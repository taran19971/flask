from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Taran'}
    posts = [
        {
            'author': {'username': 'Karan'},
            'body': 'Beautiful day in Pune!'
        },
        {
            'author': {'username': 'Sanya'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
