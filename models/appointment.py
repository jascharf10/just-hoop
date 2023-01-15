from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
#from application import Application

import arrow

class Location(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.String)
    time = db.Column(db.String)
    location = db.Column(db.String)
    location_id = db.Column(db.String)
    location_type_id = db.Column(db.String)
    location_slug = db.Column(db.String)
    hood = db.Column(db.String)
    skillrange = db.Column(db.String)
    type = db.Column(db.String)
    name = db.Column(db.String)
    statusname = db.Column(db.String)
    spotsopen = db.Column(db.String)
    price = db.Column(db.String)
    market_id = db.Column(db.String)
    reservation_id = db.Column(db.String)
    date = db.Column(db.String)
    appointments_lookup = db.relationship('Appointment', backref='Location', lazy=True)

    def __repr__(self):
        return self.location

class Appointment(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)
    spots_trigger = db.Column(db.String(50), nullable=False)
    #delta = db.Column(db.Integer, nullable=False)
    #time = db.Column(db.DateTime, nullable=False)
    #timezone = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), db.ForeignKey('games.location'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    #location_game_id = db.Column(db.Integer, db.ForeignKey('games.id'))

    def __repr__(self):
        return '<Appointment %r>' % self.name

    # def get_notification_time(self):
    #     appointment_time = arrow.get(self.time)
    #     reminder_time = appointment_time.shift(minutes=-self.delta)
    #     return reminder_time
class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    user_appointments = db.relationship('Appointment', backref='User_Id', lazy=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# @Application.login.user_loader
# def load_user(id):
#     return User.query.get(int(id))