from flask import Flask, render_template, url_for, request, redirect, url_for, abort
from .forms import RegisterForm, LoginForm
from . import main
from ..models import User, Pitch, Comments, PitchCategory, Votes
#db


app = Flask(__name__)

app.config['SECRET_KEY']= 'mine101'

pitchs = [
    {
        'id': 'id1'
        'author' : 'Trinity',
        'title': 'pitch post 1',
        'content': 'first post content',
        'date': 'feb 14, 2019'
    },
        {
        'id':'id2'
        'author': 'Race',
        'title': 'pitch post 2',
        'content': 'second post content',
        'date': 'feb 16, 2019'
    }
    ]


@main.route("/")
def home








# @app.route("/home/")
# def home():
#     return render_template('index.html', pitchs=pitchs)

@main.route("/about")
def about():
    return render_template('about.html',title='About')

@main.route("/register", methods=['GET', 'POST'])
def register():
    # if request.method == 'POST'
    #     return do_login()
    # else:
    #     return LoginForm()
    form = RegisterForm()

    return render_template('register.html', title='Register', forms=forms )

@main.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login' , forms=forms)


if __name__ =='__main__':
    app.run(debug=True)