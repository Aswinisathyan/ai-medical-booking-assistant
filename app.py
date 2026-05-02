from flask import Flask, request
from router import handle_message
from database import get_all_bookings
from flask import render_template
from flask import Flask, request, render_template
from database import get_all_bookings
import requests


app = Flask(__name__)

# 🔐 VERIFY TOKEN (must match Meta dashboard)
VERIFY_TOKEN = "mytoken"

# 🔑 Replace with your actual values from Meta
ACCESS_TOKEN = ""
PHONE_NUMBER_ID = ""


@app.route("/")
def home():
    return "WhatsApp AI Assistant Running ✅"


@app.route("/dashboard")
def dashboard():
    bookings = get_all_bookings()
    return render_template("dashboard.html", bookings=bookings)


# 📤 Send message to WhatsApp
def send_message(phone, message):
    url = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": phone,
        "text": {"body": message}
    }

    response = requests.post(url, json=data, headers=headers)

    print("📤 Send status:", response.status_code)
    print("📤 Response:", response.text)


# 🌐 Webhook
@app.route("/webhook", methods=["GET", "POST"])
def webhook():

    # 🔹 Verification (GET)
    if request.method == "GET":
        verify_token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        print("🔍 VERIFY TOKEN RECEIVED:", verify_token)

        if verify_token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return "Invalid token", 403

    # 🔹 Incoming messages (POST)
    if request.method == "POST":
        data = request.get_json()

        print("📥 Incoming data:", data)

        try:
            value = data["entry"][0]["changes"][0]["value"]

            # ✅ Handle user messages only
            if "messages" in value:
                message = value["messages"][0]

                phone = message["from"]
                text = message["text"]["body"]

                print("👤 User:", text)

                # 🧠 NLP + routing
                response_text = handle_message(text, phone)

                print("🤖 Bot:", response_text)

                # 📤 Send reply
                send_message(phone, response_text)

            else:
                print("ℹ️ Status update received, ignoring...")

        except Exception as e:
            print("❌ Error:", e)

        return "ok", 200


# ▶️ Run app
if __name__ == "__main__":
    app.run(port=5000, debug=True)