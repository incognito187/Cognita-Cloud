from flask import Flask, render_template, redirect, url_for, session, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo
import os
from datetime import datetime  # <-- Added missing import

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Simulated ECG service status
ECG_STATUS = {
    "Kumasi": "Outage",
    "Obuasi": "Outage",
    "Accra": "Outage",
}

# Ghana Town Outage Dates (for display)
OUTAGE_DATES = {
    "Kumasi": "2025-05-10",
    "Obuasi": "2025-05-12",
    "Accra": "2025-05-14",
}

def format_outage_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        day = date_obj.strftime("%A")         # Friday
        month = date_obj.strftime("%B")        # May
        year = date_obj.year                   # 2025
        day_num = date_obj.day                 # 16

        suffix = 'th' if 4 <= day_num <= 20 or 24 <= day_num <= 30 else ['st', 'nd', 'rd'][day_num % 10 - 1]
        return f"{day}, {day_num}{suffix} {month} {year}"
    except Exception:
        return "Unknown Date"

# ===== MODELS =====
class User(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    alerts = db.relationship('TownAlert', backref='user', lazy=True)

class TownAlert(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    town = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Alert Preferences
    whatsapp = db.Column(db.Boolean, default=False)
    sms = db.Column(db.Boolean, default=False)
    email = db.Column(db.Boolean, default=False)
    slack = db.Column(db.Boolean, default=False)

# ===== FORMS =====
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# ===== UTILITY FUNCTIONS =====
def get_status(town):
    return ECG_STATUS.get(town, "Power")

@app.context_processor
def utility_processor():
    return dict(get_status=get_status, format_outage_date=format_outage_date, OUTAGE_DATES=OUTAGE_DATES)

# ===== ROUTES =====
@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            session['username'] = user.username
            return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    user = User.query.filter_by(username=session['username']).first()

    selected_region = request.args.get('region')
    page = request.args.get('page', 1, type=int)
    per_page = 5

    regions = {}
    file_path = os.path.join(app.root_path, 'data', 'ghana_regions_towns.txt')
    with open(file_path, 'r') as f:
        for line in f:
            region, towns = line.strip().split(':')
            regions[region] = towns.split(',')

    towns = []
    paginated_towns = []
    total_pages = 1

    if selected_region and selected_region in regions:
        towns = regions[selected_region]
        start = (page - 1) * per_page
        end = start + per_page
        paginated_towns = towns[start:end]
        total_pages = (len(towns) + per_page - 1) // per_page

    user_alerts = [alert.town for alert in user.alerts]

    return render_template(
        'dashboard.html',
        regions=regions.keys(),
        towns=paginated_towns,
        selected_region=selected_region,
        username=session['username'],
        page=page,
        total_pages=total_pages,
        user_alerts=user_alerts
    )

@app.route('/update_alerts', methods=['POST'])
def update_alerts():
    if 'username' not in session:
        return redirect(url_for('login'))

    user = User.query.filter_by(username=session['username']).first()
    TownAlert.query.filter_by(user_id=user.id).delete()

    selected_towns = request.form.getlist('alert_town')
    for town in selected_towns:
        alert = TownAlert(town=town, user_id=user.id)
        db.session.add(alert)

    db.session.commit()
    return redirect(url_for('dashboard', region=request.form.get('region')))

@app.route('/profile')
def profile():
    if 'username' not in session:
        return redirect(url_for('login'))

    user = User.query.filter_by(username=session['username']).first()
    alerts = TownAlert.query.filter_by(user_id=user.id).all()

    return render_template('profile.html', user=user, alerts=alerts)

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    if 'username' not in session:
        return redirect(url_for('login'))

    user = User.query.filter_by(username=session['username']).first()
    alerts = TownAlert.query.filter_by(user_id=user.id).all()

    if request.method == 'POST':
        for alert in alerts:
            alert.whatsapp = bool(request.form.get(f'whatsapp_{alert.id}'))
            alert.sms = bool(request.form.get(f'sms_{alert.id}'))
            alert.email = bool(request.form.get(f'email_{alert.id}'))
            alert.slack = bool(request.form.get(f'slack_{alert.id}'))
        db.session.commit()
        return redirect(url_for('profile'))

    return render_template('edit_profile.html', alerts=alerts)

# ===== START APP =====
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=7001)