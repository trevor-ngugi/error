from flask import Flask,render_template, url_for
from app.forms import RegisterForm
from app.forms import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY']= 'mine101'

pitchhs = [
    {
        'author': 'Trinity',
        'title': 'pitch post 1',
        'content': 'first post content',
        'date_posted': 'feb 14, 2019'
    },
        {
        'author': 'Race',
        'title': 'pitch post 2',
        'content': 'second post content',
        'date_posted': 'feb 16, 2019'
    }
    ]

@app.route('/')
@app.route("/home")
def home():
    return render_template('index.html',pitchs=pitchhs)

@app.route("/about")
def about():
    return render_template('about.html',title='about')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegisterForm()
    return render_template('register.html', title='Register', forms=forms )

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login' , forms=forms)


if __name__ == '__main__':
    app.run(debug=True)
