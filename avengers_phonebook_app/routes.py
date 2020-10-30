from avengers_phonebook_app import app, db
from flask import render_template, request, redirect, url_for
from avengers_phonebook_app.forms import UserInfoForm, LoginForm, ContactPost
from avengers_phonebook_app.models import User, Post, check_password_hash
from flask_login import login_required, login_user, current_user, logout_user
@app.route('/')
def home():
    # posts = Post.query.all()
    return render_template('home.html')

@app.route('/test')
def testRoute():
    names = ['Robert','David','Bill','Jessy']
    return render_template('test.html',list_names = names)

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

        user = User(name,phone,email,password)

        db.session.add(user)

        db.session.commit()

    return render_template('register.html', user_form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        #saving the logged in user to a variable
        logged_user = User.query.filter(User.email == email).first()
        #check the password of the newly found user 
        # and validate the password against the hash value inside of the database
        if logged_user and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            #redirect user
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html', login_form = form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/posts', methods = ['GET', 'POST'])
@login_required
def posts():
    form = ContactPost()
    if request.method == 'POST' and form.validate():
        role = form.role.data
        phone_number = form.phone_number.data
        user_id = current_user.id
        post = Post(role,phone_number,user_id)

        db.session.add(post)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        db.session.rollback()
    return render_template('contactPosts.html', contact_post = form)

@app.route('/posts/<int:post_id>')
@login_required
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post_detail.html', post = post)