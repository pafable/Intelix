import urllib3
import json
http = urllib3.PoolManager()
r = http.request('GET', 'http://httpbin.org/ip')
x = json.loads(r.data.decode("utf-8"))
print(x)