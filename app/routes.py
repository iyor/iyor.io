from flask import current_app as app

@app.route('/')
@app.route('/index')
def index():
    return "Welcome to iyor.io"
