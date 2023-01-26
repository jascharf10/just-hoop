from flask import Flask
from flask_login import LoginManager

from config import config_classes
from database import db, migrate

from views import init_views


app = Flask(__name__, instance_relative_config=True)

# load the instance config, if it exists, when not testing
env = app.config.get("ENV", "production")
app.config.from_object(config_classes[env])


db.init_app(app)
migrate.init_app(app, db)
login_manager = LoginManager(app)

import tasks  # noqa E402
from models import User
# @login_manager.user_loader
# def load_user(user_id): #reload user object from the user ID 
#                         #stored in the session
#     # since the user_id is just the primary key of our user 
#     # table, use it in the query for the user
#     return User.query.get(int(user_id))
init_views(app)

