from market import app
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm
from market import db

@app.route('/') #Decorator one step before a function that is going to be executed, app route what part of the website that is going to be executed / root URL
@app.route('/home') #Multiple routes to same case
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items = items) #items when calling a list, item_name when calling a single item <table> </table> in html code, to display value we have to iterate over list
@app.route('/register', methods = ['GET','POST']) #Methods allows us to use those command from HTML
def register_page():
    form = RegisterForm()
    if form.validate_on_submit(): #Check if the user has clicked the submit button from RegisterForm. This if block should contain requirements
        user_to_create = User(username = form.username.data,
                                email_address = form.email_address.data,
                                password_hash = form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}: #If there are errors from the validation
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user {err_msg}', category = 'danger')
    return render_template('register.html', form = form)

#Jinja special template access through HTML, special designed for python web frameworks
#Don't hardcode routes, dynamic routes /page/<tag>
#@app.route('/about/<username>')
#def about_page(username):
#    return f'<h1>This is the about page of {username}</h1>'
