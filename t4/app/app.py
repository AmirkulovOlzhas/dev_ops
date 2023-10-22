from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/postgres'

db = SQLAlchemy(app)

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255))
  email = db.Column(db.String(255))

@app.route("/")
def hello_world():
    return render_template('index.html')

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
    return render_template('login.html', 
        title = 'Sign In',
        form = form)


@app.route("/user/<string:name>/<int:id>")
def user(name, id):
    return "User page: " + name + " - " + str(id)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port =int("3000"),  debug=True)