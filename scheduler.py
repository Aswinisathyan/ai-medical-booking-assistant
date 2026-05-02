import sqlite3
import time
import schedule
import requests

# 🔑 SAME values as app.py
ACCESS_TOKEN = "EAAMpNvbeI6sBRWUHBaZAIhLdjSfHUhT13ObQSFvKZB083UdkxCcf8f47fWZCHWxBB77BQhl8urmjjWJ3ns07aYIEl6s4HmDHPgTRSxllEYggGTUlyrZBUfppYpZAVAQ1gBXZCU1CDOuwpBr3SnLz1UdJd5GgthbTP3ZCk6zOHhdhxCbZBF1Bm6VvqC3ZB6LyWSroUoEFKaQncyK9cDTXcuJVRieh15Dp30kOi2pHKtmcxOg0suXTPCq1wBgZDZD"
PHONE_NUMBER_ID = "1157695764087988"



# 📤 Send WhatsApp message
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

    print("📤 Reminder sent:", response.status_code, response.text)


# 🧠 Check DB and send reminders
def check_reminders():
    conn = sqlite3.connect("lab.db")
    c = conn.cursor()

    # Get all bookings
    c.execute("SELECT phone, date, time FROM bookings")
    rows = c.fetchall()

    for phone, date, time_val in rows:

        # 🔥 SIMPLE LOGIC (for demo)
        if date == "tomorrow":
            msg = f"⏰ Reminder: Your test is scheduled tomorrow at {time_val}"
            send_message(phone, msg)

    conn.close()


# ⏱️ Run every 1 minute
schedule.every(20).minutes.do(check_reminders)


# 🔁 Infinite loop
print("⏳ Reminder Scheduler Running...")

while True:
    schedule.run_pending()
    time.sleep(1)