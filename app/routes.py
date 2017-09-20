from flask import render_template
from flask import current_app as app
from app import models

@app.route('/')
@app.route('/index')
def index():
    title = "home"
    posts = reversed(models.Post.query.all())
    return render_template('index.html',
                           title = title,
                           posts = posts)
