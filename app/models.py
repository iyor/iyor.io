import re

from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index = True, unique = True)
    # Url-friendly representation of title
    slug = db.Column(db.String(140), index = True, unique = True)
    body = db.Column(db.String())
    timestamp = db.Column(db.DateTime)

    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = self.make_slug(kwargs.get('title', ''))
        super().__init__(*args, **kwargs)

    def make_slug(self, title):
        return re.sub('[^\w]+', '-', title.lower())

    def __repr__(self):
        return "Title: %r \nSlug: %r\nTimestamp: %r" % (self.title, self.slug, self.timestamp)
