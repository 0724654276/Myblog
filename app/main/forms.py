from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import InputRequired,Email,EqualTo

class UpdateProfileForm(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Update')

class UploadBlogForm(FlaskForm):
    title = TextAreaField('Blog Title',validators=[InputRequired()])
    blog =  TextAreaField('your blog',validators=[InputRequired()])
    submit = SubmitField('Post')

class CommentsForm(FlaskForm):
    comment = TextAreaField('Type comment:',validators=[InputRequired()])
    submit = SubmitField('Comment')