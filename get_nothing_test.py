

import requests
import json

host = "https://httpbin.org/"

endpoint = 'get'

url = ''.join([host, endpoint])

'''给服务器发送请求'''
r = requests.get(url)

# print(r.text)            # unicode文本形式
# print(type(r.text))
# print(r.content)         # 二进制形式
# print(type(r.content))


# print(r.url)             # 获取url
# print(r.status_code)     # 获取状态码
# print(r.reason)          # 获取状态码原因

print(r.headers)         # 返回响应报头
print(r.request.headers)    # 返回请求消息的报头

print(r.request.method)


#########################
# 最好的方式   字典的形式
#########################
response = r.json()
print(type(response))
print(response['headers'])
print(response['headers']['Connection'])

print(eval(r.text))      # 通过eval也将其转化为字典的形式
