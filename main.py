
import requests

# payload = {'key1': 'value1', 'key2': 'value2', 'key3': None}
# r = requests.get('http://httpbin.org/get', params=payload)

r = requests.post('http://httpbin.org/post', data={'key': 'value'})
r.json()      # 返回JSON格式，可能抛出异常
print(r.url)

