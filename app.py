from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Example for Gmail
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_password'
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@gmail.com'

mail = Mail(app)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Route to send emails
@app.route('/send', methods=['POST'])
def send_email():
    subject = request.form['subject']
    body = request.form['body']
    recipients = request.form['recipients'].split(',')  # List of emails

    try:
        msg = Message(subject, recipients=recipients)
        msg.body = body
        mail.send(msg)
        flash("Emails sent successfully!", "success")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
