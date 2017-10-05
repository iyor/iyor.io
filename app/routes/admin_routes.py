import functools
from flask import render_template, Response, request, flash, redirect, url_for, session
from werkzeug.security import check_password_hash
from flask import current_app as app
from app import models, db
from app.forms import PostForm
from datetime import datetime
from app.config import ADMIN_PASS, ADMIN_USER

def login_required(fn):
    @functools.wraps(fn) # Test if this could be removed
    def inner(*args, **kwargs):
        if session.get('logged_in'):
            return fn(*args, **kwargs)
        return redirect(url_for('login', next=request.path))
    return inner

@app.route('/create', methods = ['GET', 'POST'])
@login_required
def create():
    form = PostForm()
    if form.validate_on_submit():
        post = models.Post(title = form.data['title'],
                    timestamp = datetime.utcnow(),
                    caption = form.data['caption'],
                    body = form.data['body'])
        db.session.add(post)
        db.session.commit()
        return redirect('/index')
    return render_template('create_post.html',
                           title='post',
                           form=form)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    next_url = request.args.get('next') or request.form.get('next')
    if request.method == 'POST' and request.form.get('password'):
        password = request.form.get('password')
        username = request.form.get('username')
        if check_password_hash(ADMIN_USER, username) and check_password_hash(ADMIN_PASS, password):
            session['logged_in'] = True
            session.permanent = True  # Use cookie to store session.
            flash('You are now logged in.', 'success')
            return redirect(next_url or url_for('index'))
        else:
            flash('Incorrect password.', 'danger')
    return render_template('login.html', next_url=next_url)

@app.route('/logout/', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('login'))
