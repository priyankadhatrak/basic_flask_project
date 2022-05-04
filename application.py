from users import app, handlers, config
from flask import Flask, jsonify, request

app=app.app


@app.route('/', methods=['GET'])
def helloworld():
    if(request.method == 'GET'):
        data = {"data": "hello world"}
        return jsonify(data)