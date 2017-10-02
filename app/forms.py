from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired
from app import models


class PostForm(Form):
    title = StringField('title', validators=[DataRequired()])
    body = TextAreaField('body', validators=[DataRequired()])

    def validate(self):
        if not Form.validate(self):
            return False
        post = models.Post.query.filter_by(title=self.title.data).first()
        if post is not None:
            self.title.errors.append('This title seems to be taken. '
                                        'Please choose another one.')
            return False
        return True
