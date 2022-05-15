import requests

print(requests.get('http://localhost:5000/auth', auth=('ol:aa', 'senh:a aki hehehe')).json())