from flask_wtf import FlaskForm as Form
from wtforms import TelField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = TelField('openid', validators = [DataRequired()])
    remember_me = BooleanField('remember_me', default = False)