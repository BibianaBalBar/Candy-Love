from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Abo'}
    posts = [
        {
            'author': {'username': 'Pesta'},
            'body': 'I want to go to the bedroom!'
        },
        {
            'author': {'username': 'Buda'},
            'body': 'I love rucula!'
        },
        {
            'author': {'username': 'Abo nene'},
            'body': 'We are abos!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
