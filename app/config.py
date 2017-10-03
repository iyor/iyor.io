import os

basedir = os.path.abspath(os.path.dirname(__file__))

ADMIN_PASS = 'admin_pass'

POSTS_PER_PAGE = 8

SECRET_KEY = 'my-key'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
