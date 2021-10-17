import requests

r = requests.get('https://github.com/lesstif')

print(r.status_code)
print(r.headers)
print(r.encoding)
