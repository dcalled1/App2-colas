import requests
import time
import random
import json


MIN_TIME = 2
MAX_TIME = 10
API_HOST = 'http://localhost:3000'
QUEUE = 'test1'

def prepareTask(id):
    message = input('Type the description of the task: ')
    task = {
        'task_id': id,
        'username': username,
        'email': email,
        'description': message,
    }
    time.sleep(random.randint(MIN_TIME, MAX_TIME))
    return task

def sendTask(task):
    message = json.dumps(task)
    data = {
        'username': username,
        'apiKey': apiKey,
        'message': message,
    }

    requests.post("{host}/queues/{queue}/newmessage".format(host=API_HOST, queue=QUEUE), json=data)





username = input('type the client username: ')
email = input('type the client email: ')


apiKey = requests.post(API_HOST + '/users/key/new', json={
    'username': username,
    'email': email,
})
taskCount=0
while True:
    task = prepareTask(taskCount)
    sendTask(task)
    taskCount += 1
