from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)




@app.route('/', methods = ['POST'])
def index():
    data=request.json
    option=data['option']
    if option=='':
        option=1
    option=str(option)
    
    select = {
        '1':{'ID':1,'msg': 'Hola , en que te puedo ayudar?','options':[
            {"label":"Documento","next":''},
            {"label":"Contacto","next":'2'}
        ]},
        
        '2':{'ID':2,'msg':'Bien, seleccione una opcion', 'options':[
            {"label":"Ambiental","next":'3'},
            {"label":"Urbanismo","next":'3'}
        ]},
            
        '3':{'ID':3, 'msg':'Selecione la persona con quien quiere contactarse','options':[
            {"label":"Autoridad","next":'5'},
            {"label":"Personal","next":'4'}
            
        ]},
        
        '4':{'ID':4,'msg':'Selecione al personal','options':[
            {"label":"Jorge"},
            {"label":"Arellano"},
            {"label":"Antonio"}
        ]},
        
        '5':{'ID':5,'msg':'Selecione a la autoridad','options':[
            {"label":"Gobernador","next":'6'},
            {"label":"Consejero","next":'6'},
            {"label":"Gerente","next":'6'},
            {"label":"Sub-gerete","next":'6'}
        ]},
        
        '6':{'ID':6,'msg':'Seleccione a la persona', 'options':[
            {"label":"Juan"},
            {"label":"Ruben"},
            {"label":"Adiran"}
        ]},
        '7':{'ID':7,'input':'Escriba un codigo:'},
        }
    
        
    return jsonify(select[option])


@app.route("/code", Method =['POST'])
def code ():
    o = request.json
    input = o    
    str(input("Ingrese un codigo:"))
    return input



#str(input("Ingrese el cofigo del documento:"))