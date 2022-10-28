from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)


@app.route('/', methods = ['GET'])
def index():
    if 1:
        return ['si','no']
    if 2:
        return ['si','no']
        
    return jsonify({'msg':'hi'})



@app.route ('//1', methods =['GET'])
def response():
    mensaje = ['saludos','hola']
    return jsonify (mensaje)

