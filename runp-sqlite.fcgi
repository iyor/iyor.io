#!env/bin/python
from flipflop import WSGIServer
from werkzeug.contrib.fixers import CGIRootFix
from app import app

if __name__ == '__main__':
    WSGIServer(CGIRootFix(app, app_root='/')).run()
