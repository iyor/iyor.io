from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index = True, unique = True)
    # Url-friendly representation of title
    slug = db.Column(db.String(140), index = True, unique = True)
    body = db.Column(db.String())
    timestamp = db.Column(db.DateTime)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = re.sub('[^\w]+', '-', self.title.lower())
        ret = super(Entry, self).save(*args, **kwargs)

        return ret

    def __repr__(self):
        return "Title: %r \nSlug: %r\nContent: %r\n" % (self.title, self.slug, self.body)
