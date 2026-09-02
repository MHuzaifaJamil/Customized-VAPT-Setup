#!/usr/bin/env python3
import urllib.request, urllib.error, ssl, json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def req(url, method='GET', data=None, timeout=10):
    try:
        body_data = data.encode() if isinstance(data, str) else data
        hdrs = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)',
            'Accept': 'application/json, */*',
        }
        if data:
            hdrs['Content-Type'] = 'application/x-www-form-urlencoded'
        r = urllib.request.Request(url, headers=hdrs, method=method, data=body_data)
        with urllib.request.urlopen(r, context=ctx, timeout=timeout) as resp:
            body = resp.read(5000).decode('utf-8', errors='replace')
            return resp.status, body, dict(resp.headers)
    except urllib.error.HTTPError as e:
        try: body = e.read(1000).decode('utf-8', errors='replace')
        except: body = ''
        return e.code, body, {}
    except Exception as e:
        return 0, str(e)[:80], {}

BASE = 'https://trek.nasa.gov/moon/TrekServices/ws/index'

# Test the WADL-revealed endpoints for accessibility without auth
print("=== Trek ws/index endpoint liveness tests ===")

tests = [
    '/eq/searchItems?key=*&start=0&rows=5',
    '/eq/listVisibleLayers?body=Moon',
    '/polar/listVisibleLayers?body=Moon',
    '/polar/searchItems?key=*&start=0&rows=5',
    '/getLayerServices?body=Moon',
    '/getAttachments?uuid=test',
    '/eq/getItem?body=Moon&productLabel=test',
    '/eq/searchItems?key=moon&start=0&rows=1&body=Moon',
    '/moon/eq/searchItems?key=*&start=0&rows=5',
    '/moon/eq/listVisibleLayers',
    '/moon/getLayerServices?uuid=test',
    '/moon/polar/searchItems?key=*&rows=1',
]

for path in tests:
    code, body, hdrs = req(f'{BASE}{path}')
    status_info = f'HTTP {code}'
    if code == 200:
        status_info += f' | {body[:200]}'
    elif code not in (0, 404):
        status_info += f' | {body[:100]}'
    print(f'  {path[:60]}: {status_info}')

print("\n=== WADL - Internal hostname disclosure confirmation ===")
print("Base URL disclosed: http://moontrek-protected.jpl.nasa.gov:8080/TrekServices/ws/")
print("This reveals an internal JPL host on port 8080 not reachable from internet")

print("\n=== Trek outreach WADL check (other Trek ws services) ===")
# Check if outreach still has a WADL
for svc in ['outreach', 'catalog', 'user', 'bookmark', 'annotation']:
    code, body, hdrs = req(f'https://trek.nasa.gov/moon/TrekServices/ws/{svc}', method='OPTIONS')
    if code == 200 and 'wadl' in body.lower():
        print(f'\n/moon/TrekServices/ws/{svc} OPTIONS - WADL FOUND:')
        print(body[:500])
    elif code not in (0, 404, 403):
        print(f'/moon/TrekServices/ws/{svc} OPTIONS: HTTP {code} | {body[:100]}')

print("\n=== Mars Trek index WADL ===")
code, body, hdrs = req('https://trek.nasa.gov/mars/TrekServices/ws/index', method='OPTIONS')
if code == 200:
    print(f'Mars ws/index OPTIONS: {code} | {body[:300]}')
