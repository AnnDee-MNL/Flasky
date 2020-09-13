from datetime import datetime
from flask import render_template, session, redirect, url_for, flash, abort
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from . import main
from .forms import LoginForm
from .. import db
from ..models import User


#@main.before_app_request
#def before_request():
#    if current_user.is_authenticated():
#        current_user.ping()
       

@main.route('/user/<username>')
def user(username):
 user = User.query.filter_by(username=username).first()
 if user is None:
     abort(404)
 return render_template('user.html', user=user)
