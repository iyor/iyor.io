from flask import render_template
from flask import current_app as app

@app.route('/')
@app.route('/index')
def index():
    title = "Welcome"
    posts = [
        {
            'title': 'A post',
            'synopsis': 'This is a post',
            'body': 'This is the post blablabla'
        },
        {
            'title': 'Second post',
            'synopsis': 'This is another post',
            'body': 'This is the post thing....'
        }
    ]
    return render_template('index.html',
                           title = title,
                           posts = posts)
