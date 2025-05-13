from flask import Flask, render_template, request
import smtplib
import random
from email.message import EmailMessage

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    your_name = request.form['your_name']
    crush_name = request.form['crush_name']
    chance = random.randint(0, 100)

    sender = "mad.ha207@gmail.com"  # Or use os.environ.get("EMAIL")
    password = "zdtutdzxojmlotui"   # Or use os.environ.get("EMAIL_PASSWORD")

    try:
        # Email with UTF-8 emoji support
        msg = EmailMessage()
        msg['Subject'] = "💘 Crush Match Result 💘"
        msg['From'] = sender
        msg['To'] = sender
        msg.set_content(f"{your_name} & {crush_name} have a {chance}% chance of getting married 💍")

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
        server.quit()

        print("✅ Email sent!")

        return f"""
        <div style='text-align:center; font-family: Arial, sans-serif; margin-top: 100px;'>
            <h2>💖 {your_name} & {crush_name} = {chance}% match! 💌</h2>
            
            <form action="/" method="get">
                <button style='padding: 10px 20px; font-size: 1em; background-color: #d63384; color: white; border: none; border-radius: 8px; cursor: pointer;'>🔁 Try Again</button>
            </form>
        </div>
        """

    except Exception as e:
        print("❌ Email failed:", e)
        return "❌ Failed to send email."

if __name__ == '__main__':
    app.run(debug=True)
