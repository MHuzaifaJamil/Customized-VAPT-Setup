#!/usr/bin/env python3
import urllib.request, urllib.error, ssl, json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def req(url, method='GET', data=None, timeout=10):
    try:
        body_data = data.encode() if isinstance(data, str) else data
        r = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)',
            'Accept': 'application/json, */*',
            'Content-Type': 'application/json' if data else 'text/plain'
        }, method=method, data=body_data)
        with urllib.request.urlopen(r, context=ctx, timeout=timeout) as resp:
            body = resp.read(3000).decode('utf-8', errors='replace')
            return resp.status, body, dict(resp.headers)
    except urllib.error.HTTPError as e:
        try: body = e.read(500).decode('utf-8', errors='replace')
        except: body = ''
        return e.code, body, {}
    except Exception as e:
        return 0, str(e)[:80], {}

BASE = 'https://trek.nasa.gov'

# Test ws/index with different methods
print("=== /moon/TrekServices/ws/index - method enumeration ===")
for method in ['GET', 'POST', 'PUT', 'PATCH', 'OPTIONS', 'DELETE']:
    code, body, hdrs = req(f'{BASE}/moon/TrekServices/ws/index', method=method)
    print(f'  {method}: HTTP {code} | {body[:100]}')

# Try /eq/ sub-paths on index
print("\n=== /moon/TrekServices/ws/index sub-paths ===")
subpaths = ['/eq/', '/eq/list', '/eq/search', '/eq/get', '/eq/all',
            '/eq/findAll', '/eq/findById', '/eq/count', '/eq/layers',
            '/eq/addManifest', '/eq/getManifest', '/eq/loadManifest',
            '/eq/fetchUrl', '/eq/fetch', '/eq/proxy', '/eq/request']
for sp in subpaths:
    code, body, hdrs = req(f'{BASE}/moon/TrekServices/ws/index{sp}')
    if code not in (0, 404):
        print(f'  LIVE: /moon/TrekServices/ws/index{sp} => {code}')
        print(f'    {body[:150]}')

# Try other ws/ categories that might exist
print("\n=== Other ws/ categories - moon ===")
categories = ['catalog', 'layer', 'search', 'user', 'elevation', 'footprint',
              'product', 'mosaic', 'dtm', 'imagery', 'terrain', 'projection',
              'download', 'bookmark', 'nomenclature', 'feature', 'annotation',
              'print', 'export', 'auth', 'proxy', 'fetch', 'request',
              'manifest', 'config', 'data', 'info', 'status', 'health']
for cat in categories:
    code, body, hdrs = req(f'{BASE}/moon/TrekServices/ws/{cat}')
    if code not in (0, 404):
        print(f'  LIVE: /moon/TrekServices/ws/{cat} => {code}')
        print(f'    {body[:100]}')

# Try mars (same pattern — mars also had 405 on index)
print("\n=== Mars TrekServices ws/index ===")
for method in ['GET', 'POST']:
    code, body, hdrs = req(f'{BASE}/mars/TrekServices/ws/index', method=method)
    print(f'  mars {method}: HTTP {code} | {body[:100]}')
