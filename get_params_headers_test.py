
import requests

host = "https://httpbin.org/"

endpoint = 'get'

url = ''.join([host, endpoint])

params = {'show_env':1}
headers = {'User-Agent': 'python-requests/2.18.4', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}


'''给服务器发送请求'''
r = requests.get(url, params=params, headers = headers)

print(r.status_code, r.reason)
print(r.headers)
print(r.text)

