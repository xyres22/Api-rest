from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    title = StringField('Tytul', validators=[DataRequired()])
    description = TextAreaField ('Opis')
    gatunek = StringField('Gatunek')
    done = BooleanField('Obejrzane')
