from flask import Flask, jsonify, request
from flask_cors import CORS

import webbrowser

app = Flask(__name__)
cors = CORS(app)
def url():
    webbrowser.open('http://sisgedo.regionancash.gob.pe/sisgedonew/app/main.php')
    return 


@app.route('/', methods = ['POST'])
def index():
    data=request.json
    option=data['option']
    if option=='':
        option=1
    option=str(option)
    
    select = {
        '1':{'ID':1,'msg': 'Hola , en que te puedo ayudar?','options':[
            {"label":"Documento","next":'8'},
            {"label":"Contacto","next":'2'}
        ]},
        
        '2':{'ID':2,'msg':'Bien, seleccione una opcion', 'options':[
            {"label":"Autoridad ","next":'3'},
            {"label":"Sector","next":'4'},
            {"label":"Instituciones","next":''}
        ]},
            
            
        '3':{'ID':3, 'msg':'Selecione la persona con quien quiere contactarse','options':[
            {"label":"Gobernador Regional","next":''},
            {"label":"Consejeros Regionales ","next":'7'}
            
        ]},
        
        
        '4':{'ID':4,'msg':'Selecione al personal','options':[
            {"label":"Gerencia","next":"5"},
            {"label":"Personal","next":"6"}
        ]},
        
        
        '5':{'ID':5,'msg':'Selecione a la autoridad','options':[
            {"label":"Gerente","next":'6'},
            {"label":"Sub-gerete","next":'6'}
        ]},
        
        '6':{'ID':6,'msg':'Seleccione a la persona', 'options':[
            {"label":"Gerencia General","next":''},
            {"label":"Gerencia Regional ","next":''},
            {"label":"Gerencia Regioonla de Asesoria Juridica ","next":''},
            {"label":"Gerencia Regional de Planeamiento","next":''},
            {"label":"Gerencia Regional de Desarrollo Social","next":''},
            {"label":"Gerencia Regional de Desarrollo Economico","next":''},
            {"label":"Gerencia Regional de Infraestructura","next":''},
            {"label":"Gerencia Regional de Recursos Naturales y Gestion Ambiental","next":''}
        ]},
    
        '7':{'ID':7,"msg":"Seleccione a la persona",'options':[
            {"label":"Oficina de imagen institucional","next":''},
            {"label":"Secretaria General ","next":''},
            {"label":"Oficina regional de defensa nacional","next":''}
            
            
            ]},

        "8":{"ID":8, 'msg':'<div>Ingrese al siguiente link :','href':'http://sisgedo.regionancash.gob.pe/sisgedonew/app/main.php','pass':'10'},

        "9":{"ID":9,'msg':'Ingrese al siguiente link:','href':'http://sisgedo.regionancash.gob.pe/sisgedonew/app/main.php','options':[{}]},

        "10":{"ID":10,'msg':'Deseas continuar?',"options":[
            {"label":"SI","next":"1"},
            {"label":"NO","next":"11"}
        ]},
        "11":{"ID":11, 'msg':"Adios"}
        }    
    return jsonify(select[option])


