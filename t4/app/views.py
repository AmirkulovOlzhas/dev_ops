from app import app
from flask import render_template, flash, redirect
from app.db_conn import User
from app.forms import LoginForm
from app.config import OPENID_PROVIDERS

@app.route("/")
def hello_world():
    return render_template('index.html', title = 'Home')
 
@app.route('/users')
def users():
  users = User.query.all()

  users_list = []
  for user in users:
    users_list.append({
      'id': user.id,
      'name': user.name,
      'email': user.email,
    })

  return render_template('users.html', users=users_list)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('LoginForm.html', 
        title = 'Sign In',
        form = form,
        providers = OPENID_PROVIDERS)


@app.route("/user/<string:name>/<int:id>")
def user(name, id):
    return "User page: " + name + " - " + str(id)


@app.route("/sign_up")
def sign_up():
    return render_template('signup.html', title = 'Sign Up')


@app.route("/sign_in")
def sign_in():
    return render_template('bt_login.html', title = 'Sign In')