# Just playing around with flask

# Importing Flack modules, as well as my own data module
from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from data import Articles
# added MySQL to macbook, and added Flask module to interact with it
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

# always needed
app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Luigi102!'
app.config['MYSQL_DB'] = 'myflaskapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app)


# call function Articles in data.py
Articles = Articles()

# route home screen (basically so the browser has an address to read I think
@app.route('/')

# call the html file
def index():
    return render_template('home.html')

# routes about
@app.route('/about')

def about():
    return render_template('about.html')

# routes articles
@app.route('/articles')

# adds a variable to the articles.html
def articles():
    return render_template('articles.html', articles=Articles)

# adds a variable to the address
@app.route('/article/<string:id>/')

#
def article_id(id):
    return render_template('article.html', id=id)
@app.route('/testing')

def testing():

    phrase = "Damn Zach's awesome!"
    return render_template('testing.html', phrase=phrase)

class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('confirm', message='Passwords do match')])
    confirm = PasswordField('confirm password')

@app.route('/register', methods=['GET', 'POST'])
def register():

    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt. encrypt(str(form.password.data))

        # Create cursor
        cur = mysql.connection.cursor()
        # Execute query
        columns = ('name', 'email', 'username', 'password')
        values = (name, email, username, password)
        cur.execute("""INSERT INTO users (name, email, username, password) VALUES ('%s', '%s', '%s', '%s')"""\
                    % (name, email, username, password))
        # Commit to DB
        mysql.connection.commit()
        # Close connection
        cur.close()

        flash('You are now Registered and can log in', 'success')

        redirect(url_for('index'))

    return render_template('register.html', form=form)

# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']

        # Create Cursor
        cur = mysql.connection.cursor()

        # Get user by username
        result = cur.execute("SELECT * FROM users WHERE username = %s",[username])
        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']

            # Compare Passwords
            if sha256_crypt.verify(password_candidate,password):
                # Passed
                # Create session
                session['logged_in'] = True
                session['username'] = username
                flash('You are now logged in', 'success')
                return redirect(url_for('dashboard.html')

            else:
                error = 'Invalid login'
                app.logger.info('PASSWORD MISMATCH')
                return render_template('login.html', error=error)
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template('login.html')


if __name__ =='__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)


