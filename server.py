from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ['FLASK_KEY']


@app.route('/')
def homepage():
    """View homepage"""

    return render_template('homepage.html')


@app.route('/sign-up')
def sign_up():
    """View sign up page"""

    return render_template('sign_up.html')


@app.route('/register', methods=['POST'])
def register():
    """Register a user"""

    email = request.form.get('email')
    email_confirmed = request.form.get('confirm-email')
    password = request.form.get('password')
    password_confirmed = request.form.get('confirm-password')
    profile_name = request.form.get('profile-name')
    birth_month = request.form.get('birth-month')
    birth_day = request.form.get('birth-day')
    birth_year = request.form.get('birth-year')
    gender = request.form.get('gender')

    time_created = datetime.now()

    birthday = f'{birth_year}/{birth_month}/{birth_day}'


    user = crud.get_user_by_email(email)

    if user:
        flash('Account already exists')
    elif email != email_confirmed:
        flash('emails do not match')
    elif password != password_confirmed:
        flash('passwords do not match')
    else:
        crud.create_user(email, password, profile_name, birthday, gender, time_created)

    return redirect("/login-in")

@app.route('/log-in')
def login():
    """user log in"""

    return render_template('log_in.html')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)