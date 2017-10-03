from flask import render_template, redirect, Response, url_for, abort
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

@app.route('/<slug>/')
def detail(slug):
    post = models.Post.query.filter_by(slug=slug).first()
    if post is not None:
        return render_template('detail.html', post=post)
    abort(404)

@app.errorhandler(404)
def not_found(exc):
    return Response('<h3>Not found</h3>'), 404
