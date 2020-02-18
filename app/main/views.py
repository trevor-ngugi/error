from flask import Flask, render_template, url_for, request
from forms import RegisterForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY']= 'mine101'

pitchs = [
    {
        'author': 'Trinity',
        'title': 'pitch post 1',
        'content': 'first post content',
        'date': 'feb 14, 2019'
    },
        {
        'author': 'Race',
        'title': 'pitch post 2',
        'content': 'second post content',
        'date': 'feb 16, 2019'
    }
    ]
# @app.route('/hello/')/
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)

@app.route("/")
@app.route("/home/")
def home():
    return render_template('index.html', pitchs=pitchs)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    # if request.method == 'POST'
    #     return do_login()
    # else:
    #     return LoginForm()
    form = RegisterForm()

    return render_template('register.html', title='Register', forms=forms )

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login' , forms=forms)


if __name__ =='__main__':
    app.run(debug=True)
