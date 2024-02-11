from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from models import User, db
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

app = Flask(__name__)
DB_NAME = "database.db"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
app.config['SECRET_KEY'] = 'thisisasecretkey'
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.init_app(app)
# Initialize SQLAlchemy after setting the configuration
db.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in Successfully', category="success")
                login_user(user, remember=True)
                return redirect('home')
            else:
                flash('Incorrect email or password!', category="error")
        else:
            flash('Incorrect email or password!', category="error")
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if len(email) < 4:
            flash('Email must be greater that 4 charactors.', category=('error'))
        elif len(username) < 2:
            flash('Username must be greater that 2 charactors.', category=('error'))
        elif password != confirm_password:
            flash('Passwords don\'t match.', category=('error'))
        elif len(password) < 7:
            flash('Password mutbe at least 7 lenghts.', category=('error'))
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            flash('Register Success!.', category=('success'))
            return redirect(url_for('login'))

    return render_template('register.html.j2')

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


#Drop down ของ Fated_clash ทั้ง 6

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)