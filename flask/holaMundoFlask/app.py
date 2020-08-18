from flask import Flask, request

app = Flask(__name__)


#http://localhost:5000/
@app.route('/')
def inicio():
    app.logger.info(f'Entramo al path {request.path}')
    return 'Hola mundo desde Flask !!'


@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'saludos {nombre.upper()}'

@app.route('/edad/<int:edad>')
def edad(edad):
    return f'tu edad es : {edad}'

@app.route('/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_nombre(nombre):
    return f'Tu nombre es: {nombre}'
