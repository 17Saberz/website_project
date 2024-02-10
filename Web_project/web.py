from flask import Flask, redirect, url_for, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '0293ff43f19034'
app.config['MAIL_PASSWORD'] = 'f2d89bdf1413e8'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/updates')
def updates():
    return render_template("updates.html")

@app.route('/six_desires')
def desires():
    return render_template("desires.html")

@app.route('/team')
def team():
    return render_template("team.html")

@app.route('/blog')
def blog():
    return render_template("blog.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return

#Drop down ของ Fated_clash ทั้ง 6

if __name__ == "__main__":
    app.run()