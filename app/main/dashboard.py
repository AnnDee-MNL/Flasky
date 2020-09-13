from datetime import datetime
from flask import render_template, session, redirect, url_for,flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from . import main
from .forms import LoginForm
from .. import db
from ..models import User

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))