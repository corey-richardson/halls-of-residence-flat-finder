from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, NumberRange
from wtforms import (
    StringField, 
    IntegerField,
    SelectField,
    URLField, 
    SubmitField,
    )

halls_list = sorted([
    "Radnor",
    ])

class AddUser(FlaskForm):
    name = StringField(
        "*Your Name: ",
        validators=[DataRequired()],
    )
    
    course = StringField(
        "*Your Course: ",
        validators=[DataRequired()],
    )
    
    ig = StringField(
        "Your IG: ",
    )
    sc = StringField(
        "Your SC: ",
    )
    
    hall = SelectField(
        "*Your Halls: ",
        choices = halls_list,
    )
    
    block = SelectField(
        "*Your Block Number: ",
        choices = list(range(10))
    )
    
    flat = IntegerField(
        "*Your Flat Number: ",
        validators=[
            DataRequired(),
            NumberRange(
                min=1, 
                max=20
            ),
        ],
    )
    
    room = IntegerField(
        "Your Room Number: ",
    )
    
    submit = SubmitField("Submit")
    
class FindUsers(FlaskForm):
    hall = SelectField(
        "Your Halls: ",
        choices = halls_list,
    )
    
    block = SelectField(
        "Your Block Number: ",
        choices = list(range(10))
    )
    
    flat = IntegerField(
        "Your Flat Number: ",
        validators=[
            DataRequired(),
            NumberRange(
                min=1, 
                max=20
            ),
        ],
    )
    
    submit = SubmitField()
    