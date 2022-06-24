import requests

r = requests.get('https://foodish-api.herokuapp.com/api/')
print(f'статус код: {r.status_code}')
print(f'ответ: {r.json()}')
