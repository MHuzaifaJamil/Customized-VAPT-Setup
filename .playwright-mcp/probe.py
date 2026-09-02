#!/usr/bin/env python3
import urllib.request, urllib.error, ssl, json, re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get(url, timeout=8, method='GET', data=None):
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
            'Accept': '*/*'
        }, method=method, data=data)
        with urllib.request.urlopen(req, context=ctx, timeout=timeout) as r:
            return r.status, r.read(4000).decode('utf-8', errors='replace'), dict(r.headers)
    except urllib.error.HTTPError as e:
        try: body = e.read(500).decode('utf-8', errors='replace')
        except: body = ''
        return e.code, body, {}
    except Exception as e:
        return 0, str(e)[:100], {}

# 1. spaceplace.nasa.gov API endpoints
print("=== spaceplace.nasa.gov API discovery ===")
paths = ['/api/', '/api/experiment/', '/api/quiz/', '/api/article/', '/api/fact/',
         '/api/activity/', '/api/v1/', '/api/game/', '/api/score/', '/api/user/',
         '/en/', '/en/api/', '/sitemap.xml', '/robots.txt', '/wp-json/']
for p in paths:
    code, body, hdrs = get(f'https://spaceplace.nasa.gov{p}')
    if code not in (0, 404):
        print(f'  {p}: HTTP {code} | {body[:80].strip()}')

# 2. Massloading sciencecloud - site map
print("\n=== massloading.sciencecloud.nasa.gov paths ===")
paths2 = ['/massloading/', '/massloading/data/', '/massloading/docs/', '/massloading/api/',
          '/data/', '/docs/', '/results/', '/products/', '/catalog/', '/service/']
for p in paths2:
    code, body, hdrs = get(f'https://massloading.sciencecloud.nasa.gov{p}')
    if code not in (0,):
        print(f'  {p}: HTTP {code} | {body[:60].strip()}')

# 3. Find where Cesium Sandcastle actually is (DOM XSS finding)
print("\n=== Cesium Sandcastle host search ===")
hosts = ['solarsystem.nasa.gov', 'trek.nasa.gov', 'worldwind.nasa.gov',
         'scivis.gsfc.nasa.gov', 'svs.gsfc.nasa.gov', 'cesiumjs.org',
         'cesium.gsfc.nasa.gov', 'eyes.nasa.gov', 'earthobservatory.nasa.gov']
for h in hosts:
    for p in ['/Apps/Sandcastle/', '/cesium/Apps/Sandcastle/', '/Cesium/Apps/Sandcastle/']:
        code, body, hdrs = get(f'https://{h}{p}')
        if code == 200 and 'cesium' in body.lower():
            print(f'  FOUND: https://{h}{p} => {code}')
            print(f'    Preview: {body[:100]}')

# 4. Spaceplace experiment API - other experiments
print("\n=== spaceplace.nasa.gov experiment alternatives ===")
for path in ['/api/experiment/answer/', '/api/experiment/list/', '/api/experiment/new/',
             '/api/experiment/results/', '/api/quiz/answer/', '/api/quiz/answer/new/']:
    code, body, hdrs = get(f'https://spaceplace.nasa.gov{path}')
    if code not in (0,):
        print(f'  {path}: HTTP {code} | {body[:80]}')

# 5. Trek - find remaining active endpoints
print("\n=== trek.nasa.gov remaining endpoints ===")
for planet in ['moon', 'mars', 'vesta', 'ceres']:
    for ws in ['TrekServices', 'services', 'api']:
        code, body, hdrs = get(f'https://trek.nasa.gov/{planet}/{ws}/')
        if code not in (0, 404):
            print(f'  /{planet}/{ws}/: HTTP {code} | {body[:60]}')
