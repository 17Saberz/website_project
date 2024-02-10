from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/updates')
def updates():
    return render_template("services.html")

@app.route('/six_desires')
def desires():
    return render_template("portfolio.html")

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