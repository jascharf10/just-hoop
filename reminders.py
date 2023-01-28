from flask import Flask

from config import config_classes
from database import db, migrate
from flask_login import LoginManager


app = Flask(__name__, instance_relative_config=True)
login_manager = LoginManager(app)

from views import init_views

# load the instance config, if it exists, when not testing
env = app.config.get("ENV", "production")
app.config.from_object(config_classes[env])


db.init_app(app)
migrate.init_app(app, db)
#login_manager.init_app(app)

import tasks  # noqa E402
import models# @login_manager.user_loader

# @login_manager.user_loader
# def user_loader(user_id):
#     return User.query.get(int(user_id))

# def load_user(user_id):
#     try:
#         return User.query.get(user_id)
#     except:
#         return None
init_views(app)


