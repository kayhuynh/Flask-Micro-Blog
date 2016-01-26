from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    posts = [ # fake array of posts
        {
                'author': {'nickname':'John'},
                'body': "Beautiful day in Portland!"
        },

        {
                'author':{'nickname': "Susan"},
                'body': "The Avengers movie was cool"
        }
    ]
    return render_template('index.html', user=user, posts=posts, title="Home")