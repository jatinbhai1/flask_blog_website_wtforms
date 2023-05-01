import wtforms.validators
from flask import Flask,render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,Email
from flask_bootstrap import Bootstrap
class LoginForm(FlaskForm):
    valid_mail = Email(message="Enter a valid email")

    email = StringField(label="Email", validators=[DataRequired(), valid_mail])
    password = PasswordField(label="Password" , validators=[DataRequired(), Length(min=8)])
    submit  = SubmitField(label="login")
app= Flask(__name__)
bootstrap_app = Bootstrap(app)


app.config['SECRET_KEY']="omnahamshivay_jaimahakal"
app.secret_key = "omomom"

@app.route("/")
def home():
    return render_template("index.html", bootstrap=bootstrap_app)


@app.route("/login", methods = ['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user_entered_email = login_form.email.data
        user_entered_passwrod = login_form.password.data
        print(user_entered_passwrod, user_entered_email)
        if user_entered_email == "admin@email.com" and user_entered_passwrod == "12345678":

            return render_template("success.html")
        else:
            return render_template("denied.html")


    return render_template("login.html", form = login_form)

if __name__ == "__main__":
    app.run(debug=True)
