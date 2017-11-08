# Just playing around with flask

# Importing Flack modules, as well as my own data module
from flask import Flask, render_template, flash, redirect, url_for, session, logging
from data import Articles
# added MySQL to macbook
from flask_mysqldb import MySQL
from wtforms import Form

# always needed
app = Flask(__name__)

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

if __name__ =='__main__':
    app.run(debug=True)


