from flask import Flask, request
from flask import jsonify
from model.models import *
from controller.controller import Controller

app = Flask(__name__)
controller = Controller()

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/games/', methods=['POST'])
def create_game():
    controller.create_game(request.get_data())
    response = jsonify({'some': 'data'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/games', methods=['GET'])
def get_name():
    start = request.args.get('start', None)
    number = request.args.get('number', None)
    if start is None:
        print("Full")
    print(start)
    response = jsonify(controller.get_game(start,number))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/games/edit', methods=['POST'])
def update_game():
    controller.update_game(request.get_data())
    response = jsonify({'some': 'data'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/games/remove', methods=['POST'])
def delete_game():
    controller.delete_game(request.get_data())
    response = jsonify({'some': 'data'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response  

if __name__ == "__main__":
    app.run(host='0.0.0.0')