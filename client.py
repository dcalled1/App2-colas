import requests
import time
import random
import json


MIN_TIME = 2
MAX_TIME = 10
API_HOST = 'http://localhost:3000'
QUEUE = 'test1'
APP_NAME = 'client server'

def prepareTask(id):
    description = input("Type the description of the task_{}: ".format(id))
    task = {
        'task_id': id,
        'username': username,
        'email': email,
        'description': description,
    }
    prepTime = random.randint(MIN_TIME, MAX_TIME)
    print("Preparing everything... estimated time: {} seconds".format(prepTime))
    time.sleep(prepTime)
    return task

def sendTask(task):
    message = json.dumps(task)
    data = {
        'username': username,
        'apiKey': apiKey,
        'message': message,
    }
    print("Getting ready to send:\n{}".format(data))

    requests.post("{host}/queues/{queue}/newmessage".format(host=API_HOST, queue=QUEUE), json=data)

    print("Done!")





username = input('type the client username: ')
email = input('type the client email: ')

registrationData = requests.post(API_HOST + '/users/new', json={
    'username': username,
    'email': email,
}).json()

print("Registration status:\n", registrationData)


apiKey = requests.post(API_HOST + '/users/key/new', json={
    'username': username,
    'email': email,
}).json()['apiKey']


taskCount=0
while True:
    task = prepareTask(taskCount)
    sendTask(task)
    taskCount += 1
