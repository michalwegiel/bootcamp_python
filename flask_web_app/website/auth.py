from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, add_user_to_database
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    if email == "":
        flash('Email form cannot be empty! Enter email and try again.', category='error')
    elif password == "":
        flash('Password form cannot be empty! Enter password and try again.', category='error')
    else:
        if request.method == 'POST':
            user = User.query.filter_by(email=email).first()
            if user:
                if check_password_hash(user.password, password):
                    flash('Logged in successfully!', category='success')
                    login_user(user, remember=True)
                    return redirect(url_for('views.home'))
                else:
                    flash('Invalid password, try again!', category='error')
            else:
                flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out!', category='success')
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        github = request.form.get('github')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if email == "" or first_name == "" or github == "" or password1 == "" or password2 == "":
            flash('Fill in form!', category='error')
        else:
            user = User.query.filter_by(email=email).first()
            if user:
                flash('Email already exists.', category='error')
            elif len(email) < 4:
                flash('Not valid email.', category='error')
            elif len(first_name) < 2:
                flash('First name must be greater than 1 character.', category='error')
            elif password1 != password2:
                flash('Passwords do not match.', category='error')
            elif len(password1) < 7:
                flash('Password must be at least 7 characters.', category='error')
            else:
                new_user = User(
                    email=email,
                    first_name=first_name,
                    github=github,
                    password=generate_password_hash(password1, method='sha256'),
                )
                add_user_to_database(new_user)
                flash('Account created!', category='success')
                login_user(new_user, remember=True)
                return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
