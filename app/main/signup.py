from datetime import datetime
from flask import render_template, session, redirect, url_for, flash
from . import main
from .forms import RegisterForm
from .. import db
from ..models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user


@main.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return '<h1> New user have been added to DB! </h1>'
        
    return render_template('signup.html', form=form)
