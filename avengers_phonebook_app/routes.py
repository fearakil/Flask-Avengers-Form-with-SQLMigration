from avengers_phonebook_app import app, forms
from flask import render_template, request
from avengers_phonebook_app.forms import UserInfoForm

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods = ['GET','POST'])
def register():
    #init our form
    form = UserInfoForm()
    #Validation of our form
    if request.method == 'POST' and form.validate():
        # GET Information from the form
        name = form.name.data
        phone = form.phone.data
        email = form.email.data
        password = form.password.data
        #print the data to the server that comes from the form
        print(name,phone,email,password)

    return render_template('register.html', user_form = form)