#!/usr/bin/env python3
import urllib.request, urllib.error, ssl, json, re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get(url, timeout=8, method='GET', data=None):
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)',
            'Accept': '*/*'
        }, method=method, data=data)
        with urllib.request.urlopen(req, context=ctx, timeout=timeout) as r:
            body = r.read(2000).decode('utf-8', errors='replace')
            return r.status, body, dict(r.headers)
    except urllib.error.HTTPError as e:
        try: body = e.read(200).decode('utf-8', errors='replace')
        except: body = ''
        return e.code, body, {}
    except Exception as e:
        return 0, str(e)[:80], {}

print("=== Trek TrekServices root content ===")
for planet in ['moon', 'mars', 'vesta', 'ceres']:
    code, body, hdrs = get(f'https://trek.nasa.gov/{planet}/TrekServices/')
    print(f'\n{planet}/TrekServices/ [{code}]:')
    print(body[:300])

print("\n=== Trek ws/ paths enumeration ===")
ws_cats = ['outreach', 'index', 'catalog', 'search', 'layer', 'footprint', 'user',
           'elevation', 'product', 'dataexplorer', 'download', 'bookmark',
           'nomenclature', 'feature', 'mosaic', 'dtm', 'observation', 'map',
           'auth', 'session', 'admin', 'annotation', 'print', 'export',
           'imagery', 'terrain', 'projection', 'analysis', 'tool', 'proxy']

for planet in ['moon', 'mars']:
    print(f'\n-- {planet} --')
    for ws in ws_cats:
        for sub in ['', '/eq/', '/eq/list', '/eq/search']:
            url = f'https://trek.nasa.gov/{planet}/TrekServices/ws/{ws}{sub}'
            code, body, hdrs = get(url)
            if code not in (0, 404):
                print(f'  LIVE: /{planet}/TrekServices/ws/{ws}{sub} => {code}')
                print(f'    {body[:100]}')
                break

print("\n=== Trek alternative service paths ===")
for planet in ['moon', 'mars']:
    for svc in ['services', 'api', 'rest', 'v1', 'v2', 'json']:
        code, body, hdrs = get(f'https://trek.nasa.gov/{planet}/{svc}/')
        if code not in (0, 404):
            print(f'  /{planet}/{svc}/: HTTP {code} | {body[:80]}')
