from flask import Blueprint, render_template
from flask_login import current_user, login_required
import requests

views = Blueprint('views', __name__)


def get_github_info():
    return requests.get(f'https://api.github.com/users/{current_user.github}').json()


@views.route('/')
@login_required
def home():
    github_user = get_github_info()
    return render_template("home.html", user=current_user, github_user=github_user)
