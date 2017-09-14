from flask import render_template
from flask import current_app as app

@app.route('/')
@app.route('/index')
def index():
    placeholder = {'name': 'placeholder'}
    return render_template('index.html',
                           placeholder = placeholder)
