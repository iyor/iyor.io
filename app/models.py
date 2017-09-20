from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index = True, unique = True)
    # Url-friendly representation of title
    slug = db.Column(db.String(140), index = True, unique = True)
    body = db.Column(db.String())
    timestamp = db.Column(db.DateTime)
    published = db.Column(db.Boolean(), index=True)

    def __repr__(self):
        return "Title: %r \nSlug: %r\nContent: %r" % (self.title, self.slug, self.body)
