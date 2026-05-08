import os
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

# 1. REMOVE load_dotenv() - Vercel handles this automatically
app = Flask(__name__)

# 2. Use a fallback for Secret Key so it doesn't crash if missing
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')

# --- EMAIL CONFIGURATION ---
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# 3. Use os.environ.get to prevent crashes if keys are missing
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

mail = Mail(app)

# --- ROUTES ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prices')
def prices():
    return render_template('prices.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if not name or not email or not message:
        flash("All fields are required.", "error")
        return redirect(url_for('index'))

    msg = Message(subject=f"SADU Inquiry: {name}",
                  sender=app.config['MAIL_USERNAME'],
                  recipients=[app.config['MAIL_USERNAME']])
    
    msg.body = f"New Lead Generated:\n\nName: {name}\nEmail: {email}\n\nMessage:\n{message}"
    
    try:
        mail.send(msg)
        flash("Inquiry sent successfully!", "success")
    except Exception as e:
        print(f"ERROR: {e}") 
        flash("Mail server error. Please try again.", "error")
        
    return redirect(url_for('index'))

# This is correct for Vercel
app = app
