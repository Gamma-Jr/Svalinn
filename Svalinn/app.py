from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from funcoes.interpolar_simples import interpolar
from functools import wraps

app = Flask(__name__, template_folder='library/templates',static_folder='library/static')
app.debug = True

##Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'SVALINN2018'
app.config['MYSQL_DB'] = 'Svalinn'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

##init MYSQL
mysql = MySQL(app)

#Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap (*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap


class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message = 'Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

class DataForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=50)])
    comentario = TextAreaField('Comentario', [validators.Length(min=10)])


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/sobre')
def about():
    return render_template('about.html')

@app.route('/simulacao', methods =['GET', 'POST'])
@is_logged_in
def simular():
    dados = request.form
    form = DataForm(request.form)
    if request.method == 'POST':
        modelo = request.form.get('modelo')
        variavel = request.form.get('variavel')
        x = float(request.form.get('x'))
        y = float(request.form.get('y'))
        z = float(request.form.get('z'))
        var = interpolar(modelo, variavel, x, y, z)

        title = str(session['username']+"#"+modelo+"#")
        body = request.form.get('comentario')
        tipo = 'interpolacao'
        dados = str(var)
        cur = mysql.connection.cursor()


        cur.execute("INSERT INTO dados(title, body, user, type, dados) VALUES (%s, %s, %s, %s, %s)", (title, body, session['username'], tipo, dados))

        mysql.connection.commit()

        cur.close()

        flash('Simulacao salva no banco de dados', 'success')
        return render_template('simulacao_resultado.html', var=var)

    return render_template('simulacao_simples.html')

@app.route('/dados')
@is_logged_in
def dados():
    cur = mysql.connection.cursor()

    result = cur.execute("SELECT * FROM dados")

    dados = cur.fetchall()

    if result > 0:
        return render_template('dados.html', dados = dados)
    else:
        msg = 'Nenhuma Simulacao no banco'
        return render_template('dados.html', msg = msg)

    cur.close()

@app.route('/ajuda')
def ajuda():
    return render_template('ajuda.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':

        #Get form fields
        username = request.form['username']
        password_candidate = request.form['password']

        # Create cursor
        cur = mysql.connection.cursor()

        #Get user by username
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

        if result > 0:
            #Get stored hash
            data = cur.fetchone()
            password = data['password']

            ##Compare Passwords
            if sha256_crypt.verify(password_candidate, password):
                session['logged_in'] = True
                session['username'] = username

                flash ('You are now logged in', 'success')
                return redirect(url_for('dashboard'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error = error)
            cur.close()
        else:
            error = 'Username not found'
            return render_template('login.html', error = error)
    return render_template('login.html')

@app.route('/dados/<string:id>/')
def dado(id):
    cur = mysql.connection.cursor()

    result = cur.execute("SELECT * FROM dados WHERE id = %s",[id])

    dado = cur.fetchone()

    return render_template('dado.html', dado=dado)

@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash ('You are now logged out', 'success')
    return redirect(url_for('login'))

@app.route('/dashboard')
@is_logged_in
def dashboard():
    cur = mysql.connection.cursor()

    result = cur.execute("SELECT * FROM dados")

    dados = cur.fetchall()

    if result > 0:
        return render_template('dashboard.html', dados = dados)
    else:
        msg = 'Nenhuma Simulacao no banco'
        return render_template('dashboard.html', msg = msg)

    cur.close()
    return render_template('dashboard.html')

@app.route('/registrar', methods = ['POST', 'GET'])
def registrar():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        ##Create cursor
        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO users(name, email, username, password) VALUES (%s, %s, %s, %s)", (name, email, username, password))

        ##Commit to DB
        mysql.connection.commit()

        ##close connection
        cur.close()

        flash('Esta agora registrado e pode logar', 'success')
        return redirect (url_for('login'))
    return render_template('registrar.html', form = form)

if __name__=='__main__':
    app.secret_key = 'secret123'
    app.run()
