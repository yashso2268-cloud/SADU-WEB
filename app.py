import os
from flask import Flask, render_template, request, flash, redirect, url_for # type: ignore
from flask_mail import Mail, Message # type: ignore
from dotenv import load_dotenv # type: ignore

# Load variables from .env file
load_dotenv()

app = Flask(__name__)
# Pull the secret key from the .env file
app.secret_key = os.getenv('SECRET_KEY')

# --- EMAIL CONFIGURATION ---
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True

# Pull credentials from the .env file
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

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
    # 1. Get data from the HTML form
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # 2. Basic validation
    if not name or not email or not message:
        flash("All fields are required.", "error")
        return redirect(url_for('index'))

    # 3. Create the Email Message
    msg = Message(subject=f"SADU Inquiry: {name}",
                  sender=app.config['MAIL_USERNAME'],
                  recipients=[app.config['MAIL_USERNAME']]) # Sending to yourself
    
    msg.body = f"New Lead Generated:\n\nName: {name}\nEmail: {email}\n\nMessage:\n{message}"
    
    # 4. Try to send it
    try:
        mail.send(msg)
        flash("Inquiry sent successfully! Our team will contact you shortly.", "success")
    except Exception as e:
        # This will print the error to your terminal for debugging
        print(f"DEBUGGING ERROR: {e}") 
        flash("Our mail server is busy. Please try again in a moment.", "error")
        
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)