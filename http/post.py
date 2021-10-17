import requests

r = requests.post('https://httpbin.org/post', data={'name': 'lesstif', 'key': 'value'})

print(r.status_code)
print(r.text)