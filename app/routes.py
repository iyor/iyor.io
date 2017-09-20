from flask import render_template, Response, request, flash, redirect, url_for
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

@app.route('/create/', methods = ['POST'])
def create():
    if request.form.get('title') and request.form.get('body'):
        post = models.Post(
            title = request.form['title'],
            body = request.form['body'])
        db.session.add(post)
        db.session.commit()
        flash('Entry created successfully.', 'success')
        return redirect(url_for('create', slug = post.slug))
    else:
        flash('Title and Content are required.', 'danger')
    return render_template('index.html')

@app.errorhandler(404)
def not_found(exc):
    return Response('<h3>Not found</h3>'), 404
