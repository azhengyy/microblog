from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Length
from app.models import User

class EditProfileForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    about_me = TextAreaField('个性签名', validators=[Length(min=0, max=140)])
    submit = SubmitField('确认')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validadte_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('该用户名已被使用')

class EmptyForm(FlaskForm):
    submit = SubmitField('关注/取消关注')

class PostForm(FlaskForm):
    post = TextAreaField('写微博', validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('发布')