
import requests

host = "https://httpbin.org/"

endpoint = 'get'

url = ''.join([host, endpoint])

params = {'show_env':1}

'''给服务器发送请求'''
r = requests.get(url, params=params)

print(r.status_code, r.reason)
print(r.headers)
print(r.text)
# print(r.request.headers)

