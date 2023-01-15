from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, SelectField, SelectMultipleField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length
from pytz import common_timezones
#from reminders import create_app
#from database import db
from models.appointment import Appointment, Location


# from database import db
# from sqlalchemy import create_engine

# engine = create_engine("postgresql://postgres:password@localhost/appointments")
# connection = engine.connect()

# my_query = 'SELECT location FROM "games" order by location desc'
# locations = connection.execute(my_query).fetchall()

def _timezones():
    return [(tz, tz) for tz in common_timezones][::-1]

# app = create_app()

# def _locations():
#     with app.app_context():
#         db.create_all()
#         return [(game.location) for game in Location.query.all()]

# all_locations = _locations()
# # all_locations = db.session.query(Location).all()

spots_trigger = [(t, t + " spots left") for t in ['1', '2', '3', '4']]


class NewAppointmentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone_number = StringField('Phone number', validators=[DataRequired(), Length(min=5)])
    spots_trigger= SelectField(
        'Spots Trigger', choices=spots_trigger, validators=[DataRequired()]
    )
    #time = DateTimeField(
    #    'Appointment time', validators=[DataRequired()], format="%m-%d-%Y %I:%M%p"
    #)
    location = SelectMultipleField('Location', validators=[DataRequired()])
    #location = QuerySelectField(
    #    'Location',
    #    query_factory=lambda: Location.query)
    #id = StringField('Id', validators=[DataRequired()])