from flask import render_template, redirect, Response, url_for
from flask import current_app as app
from app import models, db

@app.route('/')
@app.route('/index')
def index():
    title = "home"
    posts = reversed(models.Post.query.all())
    return render_template('index.html',
                           title = title,
                           posts = posts)

@app.errorhandler(404)
def not_found(exc):
    return Response('<h3>Not found</h3>'), 404
