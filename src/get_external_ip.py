import json
import urllib3

http = urllib3.PoolManager()
request = http.request('GET', 'http://ip.jsontest.com')

if (request.status >= 400):
  print("Could not retrieve external IP address")
  exit(1)

result = json.loads(request.data)
ip = result["ip"]

print("Your external IP address is {}".format(ip))
