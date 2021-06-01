import requests
import time
import random
import json


MIN_TIME = 2
MAX_TIME = 10
API_HOST = 'http://localhost:3000'
QUEUE = 'testyqueue'
APP_NAME = 'testyAppy'

def receiveTask():
    print("trying to get tasks...")
    data = {
        'username': username,
        'apiKey': apiKey
    }
    r = requests.post(url="{host}/queues/{queue}/getmessage".format(host=API_HOST, queue=QUEUE), json=data).json()
    while not bool(r):
        r = requests.post(url="{host}/queues/{queue}/getmessage".format(host=API_HOST, queue=QUEUE), json=data).json()
        time.sleep(1)
    
    task = json.loads(r['message'])
    print("task {id} founded. Description: {desc}".format(id=task['task_id'], desc=task['description']))
    
    return task

def doTask(task):
    taskTime = random.randint(MIN_TIME, MAX_TIME)
    print("Doing task {id}. Estimated time: {time} seconds.".format(id=task['task_id'], time=taskTime))
    time.sleep(taskTime)
    print("Task {id} Done!.".format(id=task['task_id']))






username = input('type the server username: ')
email = input('type the server email: ')

registrationData = requests.post(API_HOST + '/users/new', json={
    'username': username,
    'email': email,
}).json()

print("Registration status:\n", registrationData)


apiKey = requests.post(API_HOST + '/users/key/new', json={
    'username': username,
    'email': email,
    'appname': APP_NAME,
}).json()['apiKey']

print("apiKey: {}".format(apiKey))

while True:
    task = receiveTask()
    doTask(task)
