from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/postgres'

db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255))
  email = db.Column(db.String(255))

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/users')
def users():
  users = User.query.all()

  # Преобразуем полученные данные в список словарей

  users_list = []
  for user in users:
    users_list.append({
      'id': user.id,
      'name': user.name,
      'email': user.email,
    })

  # Отображаем данные в шаблоне Flask

  return render_template('./app/users.html', users=users_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port =int("3000"),  debug=True)