from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

from queues import queues

@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"pong!"})

@app.route('/users', methods=["GET"])
def getusers():
    users = requests.get('http://127.0.0.1:3000/users')
    return jsonify(users.text)

@app.route('/queues', methods=["GET"])
def getqueues():
    r = requests.get('http://127.0.0.1:3000/queues')
    return jsonify(r.text)

@app.route("/queues/<int:queueid>/<string:newmessage>", methods=["POST"])
def getqueue(queueid):
    queue = requests.get('http://127.0.0.1:3000/queues/:queueid/newmessage')
    if (len(queue) > 0):
        return jsonify({"Queue": queuesFound[0]})
    return jsonify({"message": "Queue not found :("})

@app.route("/queues/<string:queues_username>", methods=["GET"])
def getqueue(queues_username):
    queueFound = [queues for queues in queues if queues["username"] == queues_username]
    if (len(queueFound) > 0):
        return jsonify({"Queue": queuesFound[0]})
    return jsonify({"message": "Queue not found :("})

@app.route("/queues/newqueue/<string:queuename>", methods=["POST"])
def addqueue(queuename):
    new_queue = {
        "name": queuename, 
        "owner": request.json["userA"]
    }
    queues.append(new_queue)
    return jsonify({"message": "Queue added succesfully :)", "queues": queues})

if __name__ == "__main__":
    app.run(debug=True, port=4000)