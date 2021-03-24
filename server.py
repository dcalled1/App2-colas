import requests
import time
import random
import json


MIN_TIME = 2
MAX_TIME = 10
API_HOST = 'http://localhost:3000'
QUEUE = 'test1'
APP_NAME = 'client server'

def receiveTask():
    print("trying to get tasks...")
    r = requests.get(url="{host}/queues/{queue}/getmessage".format(host=API_HOST, queue=QUEUE)).json()
    while not bool(r):
        r = requests.get(url="{host}/queues/{queue}/getmessage".format(host=API_HOST, queue=QUEUE)).json()
        time.sleep(1)
    
    task = json.loads(r['message'])
    print("task {id} founded. Description: {desc}".format(id=task['id'], desc=task['description']))
    
    return task

def doTask(task):
    taskTime = random.randint(MIN_TIME, MAX_TIME)
    print("Doing task {id}. Estimated time: {time} seconds.".format(id=task['id'], time=taskTime))
    time.sleep(taskTime)






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
