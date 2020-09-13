import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_wtf import RecaptchaField
from config import config
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'main.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'
    
    with app.app_context():
        db.create_all()

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app