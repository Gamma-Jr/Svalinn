from flask import Flask, render_template, flash, redirect, url_for, session, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from funcoes.interpolar_simples import interpolar

app = Flask(__name__, template_folder='library/templates',static_folder='library/static')
app.debug = True


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/sobre')
def about():
    return render_template('about.html')

@app.route('/simulacao', methods =['GET', 'POST'])
def simular():
    dados = request.form
    if request.method == 'POST':
        modelo = request.form.get('modelo')
        variavel = request.form.get('variavel')
        x = float(request.form.get('x'))
        y = float(request.form.get('y'))
        z = float(request.form.get('z'))
        var = interpolar(modelo, variavel, x, y, z)
        return render_template('simulacao_resultado.html', var=var)

    return render_template('simulacao_simples.html')

@app.route('/projeto')
def projeto():
    return render_template('projeto.html')

@app.route('/ajuda')
def ajuda():
    return render_template('ajuda.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')


if __name__=='__main__':
    app.run()
