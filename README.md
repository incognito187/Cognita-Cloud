# Cognita-Cloud

🎉 Great! You want the **final full-featured Flask app** with:

✅ Email-based registration  
✅ Session timeout/logout on inactivity  
✅ Admin dashboard  
✅ PostgreSQL support  
✅ Bootstrap UI  
✅ Password hashing  
✅ Flash messages  
✅ Profile settings  
✅ Auto-generated folder structure  
✅ Downloadable ZIP  

You **don’t** want OAuth integration (Google/Facebook), so we’ll skip that.

---

## 📦 Final Project Structure

```
flask_auth_app/
│
├── app.py
├── requirements.txt
└── templates/
    ├── base.html
    ├── home.html
    ├── login.html
    ├── profile.html
    ├── register.html
    └── admin.html
```

I’ll now give you a **Python script** to auto-generate this project structure, and then I’ll provide the full downloadable ZIP-like content below.

---

## 🧪 Step 1: Python Script to Generate Folder Structure

Create a file called `generate_project.py`:

```python
import os

project_name = "flask_auth_app"
os.makedirs(project_name, exist_ok=True)
os.makedirs(os.path.join(project_name, "templates"), exist_ok=True)

# Create requirements.txt
with open(os.path.join(project_name, "requirements.txt"), "w") as f:
    f.write("Flask==3.0.0\n")
    f.write("Flask-SQLAlchemy==3.1.1\n")
    f.write("Flask-Login==0.6.2\n")
    f.write("psycopg2-binary==2.9.9\n")

# Create app.py
app_py_content = '''from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flaskuser:flaskpass@localhost/flaskauthdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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
    session.permanent = True
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

@app.route('/logout')
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
'''

with open(os.path.join(project_name, "app.py"), "w") as f:
    f.write(app_py_content)

# Create template files

template_base = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Flask Auth App{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }
        .sidebar {
            background-color: #2c3e50;
            color: white;
            min-height: 100vh;
        }
        .sidebar a {
            color: white;
            text-decoration: none;
        }
        .content {
            padding: 20px;
        }
    </style>
</head>
<body>

<nav class="navbar navbar-dark bg-primary mb-4">
    <div class="container-fluid">
        <a class="navbar-brand" href="#">LiveStream Dashboard</a>
    </div>
</nav>

<div class="d-flex">
    <div class="sidebar p-3 col-md-2">
        <h4>Menu</h4>
        <ul class="nav flex-column">
            <li class="nav-item"><a class="nav-link" href="{{ url_for('home') }}">Home</a></li>
            <li class="nav-item"><a class="nav-link" href="{{ url_for('profile') }}">Profile</a></li>
            {% if current_user.is_admin %}
            <li class="nav-item"><a class="nav-link" href="{{ url_for('admin') }}">Admin</a></li>
            {% endif %}
            <li class="nav-item">
                <form action="{{ url_for('logout') }}" method="post">
                    <button type="submit" class="btn btn-danger w-100">Logout</button>
                </form>
            </li>
        </ul>
    </div>

    <div class="content col-md-10">
        {% with messages = get_flashed_messages() %}
          {% if messages %}
            <div class="alert alert-info">
              {% for message in messages %}
                {{ message }}
              {% endfor %}
            </div>
          {% endif %}
        {% endwith %}
        {% block content %}{% endblock %}
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
'''

with open(os.path.join(project_name, "templates", "base.html"), "w") as f:
    f.write(template_base)

template_home = '''{% extends "base.html" %}
{% block title %}Welcome{% endblock %}
{% block content %}
<h1>Welcome, {{ username }}!</h1>
<p>This is your dashboard after logging in.</p>
{% endblock %}
'''

with open(os.path.join(project_name, "templates", "home.html"), "w") as f:
    f.write(template_home)

template_profile = '''{% extends "base.html" %}
{% block title %}Profile{% endblock %}
{% block content %}
<h2>Profile Settings</h2>
<form method="POST">
    <div class="mb-3">
        <label for="old_password" class="form-label">Current Password</label>
        <input type="password" name="old_password" class="form-control" required>
    </div>
    <div class="mb-3">
        <label for="new_password" class="form-label">New Password</label>
        <input type="password" name="new_password" class="form-control" required>
    </div>
    <button type="submit" class="btn btn-primary">Change Password</button>
</form>
{% endblock %}
'''

with open(os.path.join(project_name, "templates", "profile.html"), "w") as f:
    f.write(template_profile)

template_register = '''{% extends "base.html" %}
{% block title %}Register{% endblock %}
{% block content %}
<h2>Register</h2>
<form method="POST">
    <div class="mb-3">
        <label for="username" class="form-label">Username</label>
        <input type="text" name="username" class="form-control" required>
    </div>
    <div class="mb-3">
        <label for="email" class="form-label">Email address</label>
        <input type="email" name="email" class="form-control" required>
    </div>
    <div class="mb-3">
        <label for="password" class="form-label">Password</label>
        <input type="password" name="password" class="form-control" required>
    </div>
    <button type="submit" class="btn btn-success">Register</button>
</form>
<p>Already have an account? <a href="{{ url_for('login') }}">Log in</a></p>
{% endblock %}
'''

with open(os.path.join(project_name, "templates", "register.html"), "w") as f:
    f.write(template_register)

template_login = '''{% extends "base.html" %}
{% block title %}Login{% endblock %}
{% block content %}
<h2>Login</h2>
<form method="POST">
    <div class="mb-3">
        <label for="email" class="form-label">Email address</label>
        <input type="email" name="email" class="form-control" required>
    </div>
    <div class="mb-3">
        <label for="password" class="form-label">Password</label>
        <input type="password" name="password" class="form-control" required>
    </div>
    <button type="submit" class="btn btn-primary">Login</button>
</form>
<p>Don't have an account? <a href="{{ url_for('register') }}">Register</a></p>
{% endblock %}
'''

with open(os.path.join(project_name, "templates", "login.html"), "w") as f:
    f.write(template_login)

template_admin = '''{% extends "base.html" %}
{% block title %}Admin Dashboard{% endblock %}
{% block content %}
<h2>Admin Dashboard</h2>
<table class="table table-striped">
    <thead>
        <tr>
            <th>ID</th>
            <th>Username</th>
            <th>Email</th>
            <th>Is Admin</th>
        </tr>
    </thead>
    <tbody>
        {% for user in users %}
        <tr>
            <td>{{ user.id }}</td>
            <td>{{ user.username }}</td>
            <td>{{ user.email }}</td>
            <td>{{ 'Yes' if user.is_admin else 'No' }}</td>
        </tr>
        {% endfor %}
    </tbody>
</table>
{% endblock %}
'''

with open(os.path.join(project_name, "templates", "admin.html"), "w") as f:
    f.write(template_admin)

print(f"✅ Project '{project_name}' generated successfully!")
```

---

## 📦 How to Use It

1. Run the script:
   ```bash
   python generate_project.py
   ```

2. A folder named `flask_auth_app` will be created with all files.

3. Install dependencies:
   ```bash
   cd flask_auth_app
   pip install -r requirements.txt
   ```

4. Set up PostgreSQL:
   ```sql
   CREATE USER flaskuser WITH PASSWORD 'flaskpass';
   CREATE DATABASE flaskauthdb OWNER flaskuser;
   ```

5. Start the app:
   ```bash
   python app.py
   ```

6. Access it at [http://localhost:5000](http://localhost:5000)

---

## ✅ Features Recap

| Feature | Status |
|--------|--------|
| Email-based Registration | ✅ Done |
| Session Timeout | ✅ Done |
| Admin Dashboard | ✅ Done |
| PostgreSQL Support | ✅ Done |
| Bootstrap UI | ✅ Done |
| Password Hashing | ✅ Done |
| Flash Messages | ✅ Done |
| Profile Settings | ✅ Done |

---

Would you like me to:
- Package this into a downloadable ZIP?
- Add REST API endpoints for mobile apps?
- Provide a Dockerfile for easy deployment?

Let me know how you'd like to proceed!