from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth',__name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", text="Testing")


@auth.route('/contact')
def logout():
    data = request.form
    print(data)
    return render_template("contact.html")


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('Email')
        firstname = request.form.get('Firstname')
        secondname = request.form.get('Secondname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(firstname) < 3:
            flash('First name must be longer than 3 characters.', category='error')
        elif len(email) < 4:
            flash('Email must be longer than 4 characters.', category='error')
        elif password1 != password2:
            flash("Your passwords doesn't match.", category='error')
        elif len(password1) < 8:
            flash('Your password must not contain less than 8 characters.', category='error')
        else:
            flash('Account created!', category='success')


    return render_template("signup.html")

