from flask import Blueprint

main = Blueprint('main', __name__)

from . import home, errors, signup, login, dashboard, user
from ..models import Permission

@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)