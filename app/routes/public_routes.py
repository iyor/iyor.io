from flask import render_template, redirect, Response, url_for, abort
from flask import current_app as app
from app import models, db
from app.config import POSTS_PER_PAGE

@app.route('/')
@app.route('/index')
@app.route('/index/<int:page>')
def index(page=1):
    title = "home"
    posts = (
        models.Post.query.order_by(models.Post.timestamp.desc())
        .paginate(page, POSTS_PER_PAGE, False)
    )
    return render_template('index.html',
                           title = title,
                           posts = posts)

@app.route('/about')
def about():
    title = "about"
    return render_template('about.html',
                           title = title)

@app.route('/<slug>/')
def detail(slug):
    post = models.Post.query.filter_by(slug=slug).first()
    if post is not None:
        return render_template('detail.html', post=post)
    abort(404)

@app.errorhandler(404)
def not_found(exc):
    return Response('<h3>Not found</h3>'), 404
