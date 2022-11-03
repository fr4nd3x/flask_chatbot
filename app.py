from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)




@app.route('/', methods = ['POST'])
def index():
    request.json 
    select = {
        '1':{'ID':1,'msg': 'Hola, en que te puedo ayudar?','options':["Documento","Contacto"]},
        '2':{'ID':2,'msg':'Bien, seleccione una opcion', 'Options':["Ambiente", "Urbanismo"]},
        '3':{'ID':3, 'msg':'Selecione la persona con quien quiere contactarse','Options':["Autoridad","Personal"]},
        '4':{'ID':4,'msg':'Selecione al personal','Option':["Jorge","Arellano","Antonio"]}
        }
    return jsonify(select['1'])









@app.route('/contact', methods = ['POST'])
def ins():
    request.json 
    map = {
        '1':{'ID':2,'msg': 'bien','options':["Ambiente","Urbanismo"]},
        }
    return jsonify(map['1'])


@app.route('/ambi', methods = ['POST'])
def ambi():
    request.json 
    map = {
        '1':{'ID':2,'msg': 'ok','options':["Gerente","Sub-Gerente"]},
        }
    return jsonify(map['1'])




@app.route('/gere', methods = ['POST'])
def des():
    request.json 
    map = {
        '1_A1':{'ID':4,'msg': 'Nombre del las personas ','options':["Valeria ","Arellano","Pedro"]},
        
    }
    
    return jsonify(map['1_A1'])

@app.route ('/sub', methods = [ 'POST'])
def sub():
    request.json
    map = {
        '1':{'ID':5, 'msg':'nada','options':["Nombre1","Nombre2","Nombre3"]}
    }
    return jsonify(map['1'])








@app.route('/4', methods = ['GET'])
def anex():
    request.json 
    map = {
        
        '1_A':{'ID':2,'msg': 'bien','options':["Ambiente","Urbanismo"]},
        '1_B':{'ID':3,'msg': 'otro','options':["Gerente","Sub-Gerente"]},
        
    }
    
    return jsonify(map['1'])






















@app.route ('/1', methods =['GET'])
def response():
    mensaje = ['saludos','hola']
    return jsonify (mensaje)

"""@app.route ('//1', methods =['GET'])
def mm ():
    """