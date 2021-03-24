import requests


def receiveTask():
    pass


def doTask(task):
    pass




API_HOST = 'http://localhost:3000'


username = input('type the consumer username')
email = input('type the consumer email')


apiKey = requests.post(API_HOST + '/users/key/new', json={
    'username': username,
    'email': email,
})

while True:
    task = receiveTask()
    doTask(task)

