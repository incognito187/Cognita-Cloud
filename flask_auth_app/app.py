# app.py

from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

# PostgreSQL DB URI (update this for your environment)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flaskuser:flaskpass@localhost/flaskauthdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Session Timeout (e.g., 5 minutes)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.before_request
def before_request():
    session.permanent = True  # Make session last across browser restarts
    app.permanent_session_lifetime = app.config['PERMANENT_SESSION_LIFETIME']

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        existing_user = User.query.filter_by(username=username).first()
        existing_email = User.query.filter_by(email=email).first()

        if existing_user or existing_email:
            flash("Username or email already exists")
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! Please log in.")
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            session['user_id'] = user.id
            return redirect(url_for('home'))
        else:
            flash("Invalid email or password")
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('login'))


@app.route('/home')
@login_required
def home():
    return render_template('home.html', username=current_user.username)

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        old_password = request.form['old_password']
        new_password = request.form['new_password']
        if not check_password_hash(current_user.password, old_password):
            flash("Old password is incorrect")
            return redirect(url_for('profile'))
        current_user.password = generate_password_hash(new_password)
        db.session.commit()
        flash("Password updated successfully")
        return redirect(url_for('profile'))
    return render_template('profile.html', username=current_user.username)

@app.route('/admin')
@login_required
def admin():
    if not current_user.is_admin:
        flash("You don't have access to this page.")
        return redirect(url_for('home'))
    users = User.query.all()
    return render_template('admin.html', users=users)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

# Sample data: group external URLs by category
def load_services(filename):
    try:
        with open(filename, 'r') as f:
            services = []
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if " " in line:
                    name, url = line.split(" ", 1)
                else:
                    url = line
                    name = url.replace("https://status.",  "").replace(".com", "")
                services.append((name, url))
            return services
    except FileNotFoundError:
        return []
@app.route('/saas')
@login_required
def saas():
    return render_template('cloud_service.html', title="SaaS", services=load_services("SaaS.txt"))

@app.route('/paas')
@login_required
def paas():
    return render_template('cloud_service.html', title="PaaS", services=load_services("PaaS.txt"))

@app.route('/iaas')
@login_required
def iaas():
    return render_template('cloud_service.html', title="IaaS", services=load_services("IaaS.txt"))