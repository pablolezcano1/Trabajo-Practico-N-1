from flask import Flask
from flask import render_template
from flask import redirect
import uuid
from os import path, getcwd
from pathlib import Path
from functions import leer_datos
import requests

app = Flask(__name__)
data = leer_datos(f'{getcwd()}/data/datos.csv')
title = 'Prueba de App en Flask'

@app.route("/")
@app.route('/home')
def index():
    context = {'lastName':'Cazabat',
               'firstName':'Danie´l',
               'age':53,
               'data': data}
    return render_template('index.html',context=context, title=title)

@app.route('/page2')
def page2():
    iduuid = uuid.uuid4()
    return render_template('page2.html', iduuid=iduuid, data=data)

@app.route('/page3')
@app.route('/page3/<string:id>')
def page3(id=''):
    data = [1,2,3,5,6,8,9]
    print(id)
    if id:
        return render_template('page3.html', id=id)
    return render_template('page3.html', data=data)

@app.route('/datos/<int:id>')
def datoscliente(id=0):
    if id:
        if len(data) >= id:
            context = {'exist':True, 'data': data[id-1]}
        else:
            context = {'exist': False}
    return render_template('datos.html', context=context, title= title)

@app.route('/products')
def products():
    endpoint_url = 'https://fakestoreapi.com/products'
    response = requests.get(endpoint_url)
    data = response.json()
    context = {'data': data,
               'title': 'Productos'}
    return render_template('products.html', context=context)

if __name__ == '__main__':
    app.run(debug=True)