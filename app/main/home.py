from datetime import datetime
from flask import render_template, session, redirect, url_for, flash, send_file
from . import main
from .. import db
from ..models import User

@main.route('/')
def index():
    return render_template('index.html')