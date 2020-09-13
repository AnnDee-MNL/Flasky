from datetime import datetime
from flask import render_template, session, redirect, url_for,flash
from . import main
from .forms import LoginForm
from .. import db
from ..models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('main.dashboard'))
        return '<h1> Invalid username or password </h1>'

    return render_template('login.html', form=form)
