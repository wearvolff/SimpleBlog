from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class PostForm(FlaskForm):
    title = StringField('Заголовок', validators=[validators.Length(min=5, max=150, message="Длинна должна быть больше 5 символов")])
    text = TextAreaField('Текст', validators=[validators.Length(min=5, max=2000, message= "Длина больше 2000 сиволов")])

class CommentForm(FlaskForm):
    text = TextAreaField('Коментарий', validators=[validators.input_required, validators.length(min=2, max=250)])