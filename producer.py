import requests

API_HOST = 'http://localhost:3000'


username = input('type the producer username')
email = input('type the producer email')


apiKey = requests.post(API_HOST + '/users/key/new', json={
    'username': username,
    'email': email,
})

while True:
    pass
