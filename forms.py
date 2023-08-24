from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, NumberRange
from wtforms import (
    StringField,
    IntegerField,
    SelectField,
    SubmitField,
    )

halls_list = sorted([
    "Radnor",
    "Francis Drake",
    "Gilwell",
    "Mary Newman",
    "Pilgrim",
    "Robbins",
    "Saltwater",
    "Beckley Point",
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
        default="Radnor",
    )

    block = StringField(
        "*Your Block Number/Letter: ",
        validators=[DataRequired()],
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
        "*Your Room Number: ",
        validators=[DataRequired()],
    )

    submit = SubmitField("Submit")

class FindUsers(FlaskForm):
    hall = SelectField(
        "Your Halls: ",
        choices = halls_list,
        default="Radnor",
    )

    block = StringField(
        "Your Block Number/Letter: ",
        validators=[DataRequired()],
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
