from flask import Flask,render_template, url_for
app = Flask(__name__)
#
pitchhs = [
    {
        'author': 'Trinity',
        'title': 'blog post 1',
        'content': 'first post content',
        'date_posted': 'feb 14, 2019'
    },
        {
        'author': 'Race',
        'title': 'blog post 2',
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
    return render_template('about.html',title=about)
if __name__ == '__main__':
    app.run(debug=True)
