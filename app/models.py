import re
from flask import Markup
from markdown import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.extra import ExtraExtension
from micawber import bootstrap_basic, parse_html
from micawber.cache import Cache as OEmbedCache

from app import db

oembed_providers = bootstrap_basic(OEmbedCache())

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index = True, unique = True)
    # Url-friendly representation of title
    slug = db.Column(db.String(140), index = True, unique = True)
    body = db.Column(db.String())
    timestamp = db.Column(db.DateTime)

    @property
    def html_body(self):
        hilite = CodeHiliteExtension(linenums=False, css_class='highlight')
        extras = ExtraExtension()
        markdown_content = markdown(self.body, extensions=[hilite, extras])
        oembed_content = parse_html(
            markdown_content,
            oembed_providers,
            urlize_all=True,
            maxwidth=600)
        return Markup(oembed_content)

    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = self.make_slug(kwargs.get('title', ''))
        super().__init__(*args, **kwargs)

    def make_slug(self, title):
        return re.sub('[^\w]+', '-', title.lower())

    def __repr__(self):
        return "Title: %r \nSlug: %r\nTimestamp: %r" % (self.title, self.slug, self.timestamp)
