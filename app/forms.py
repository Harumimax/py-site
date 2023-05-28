import email_validator
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, Email

class FindEmail(FlaskForm):
    email = StringField(
        'Введите Email',
        validators=[Email(message='Введите email'), Length(max=30, message='Введите Емаил длиной до 30 символов')]
    )
    submit = SubmitField('Искать запросы')

class NewsForm(FlaskForm):
    name = StringField(
        'Имя пользователя',
        validators=[DataRequired(message="Поле не должно быть пустым"),
                    Length(max=10, message='Введите заголовок длиной до 10 символов')]
    )
    email = StringField(
        'Email для уведомления',
        validators=[Email(message='Введите email'), Length(max=30, message='Введите Емаил длиной до 30 символов')]
    )
    good = StringField(
        'Введите название товара',
        validators=[DataRequired(message="Поле не должно быть пустым"),
                    Length(max=255, message='Введите заголовок длиной до 255 символов')]
    )
    discount = StringField(
        'Введите желаюемую скидвку, в %',
        validators=[DataRequired(message="Поле не должно быть пустым"),
                    Length(max=2, message='От 0 до 99, без %')]
    )

    submit = SubmitField('Добавить запрос')