from flask import render_template, Response, request, flash, redirect, url_for
from flask import current_app as app
from app import models, db
from app.forms import PostForm
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    title = "home"
    posts = reversed(models.Post.query.all())
    return render_template('index.html',
                           title = title,
                           posts = posts)

@app.route('/create', methods = ['GET', 'POST'])
def create():
    form = PostForm()
    if form.validate_on_submit():
        post = models.Post(title = form.data['title'],
                    timestamp = datetime.utcnow(),
                    body = form.data['body'])
        db.session.add(post)
        db.session.commit()
        return redirect('/index')
    return render_template('create_post.html',
                           title='post',
                           form=form)

@app.errorhandler(404)
def not_found(exc):
    return Response('<h3>Not found</h3>'), 404
