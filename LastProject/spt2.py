import json
from urllib.request import urlopen

import speedtest
from django.db.models.fields import files

info = json.loads(urlopen("http://ip-api.com/json/").read().decode('utf-8'))
test = speedtest.Speedtest()
print("loading server list...")
test.get_servers() #Get list servers
print("Choosing best server...")
best = test.get_best_server()
print(best)
print(f"Found: {best['host']} located in {best['country']}")
print(f"Your regionName: {info['regionName']}, {info['city']} city")
print(f"Time zone: ({info['timezone']})")
print(f"Testing from {info['org']} - {info['isp']} ({info['query']})")
print(f"Hosted: {best['sponsor']} place in {best['name']}")
print("Performing download test...")
download_result = test.download()
print(f"Download speed: {download_result/1024/1024:.2f} Mbit/s")
print("Performing upload test...")
upload_result = test.download()
print(f"Upload speed: {upload_result/1024/1024:.2f} Mbit/s")
print("Performing ping...")
ping_result = test.results.ping
print(f"Ping: {ping_result:.2f} ms")

# import urllib.request
# from urllib.request import urlopen
# import json
# external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
# external_name = urllib.request.urlopen("http://ip-api.com/json/").read().decode('utf8')
# info = json.loads(urlopen("http://ip-api.com/json/").read().decode('utf-8'))
# print(external_ip)
# print(external_name)
# print(info['org'])

