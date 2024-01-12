from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, Email, DataRequired


class HiremeForm(FlaskForm):
    name = StringField(label='name', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='email', validators=[Email(), Datarequired()])
    msg = StringField(label='msg', validators=[Length(min=10, max=1000),DataRequired()])
    submit=SubmitField(label="submit")

