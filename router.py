from nlp_engine import predict
from entity_extractor import extract_datetime
from database import save_booking
from api import call_api

def handle_message(msg, phone=None):

    intent, confidence = predict(msg)

    print("Intent:", intent, "Confidence:", confidence)

    # 🟢 HIGH confidence → use model + rules
    if confidence >= 0.7:

        if intent == "booking":

            date, time = extract_datetime(msg)

            if date and time:
                save_booking(phone, msg, date, time)
                return f"Booking confirmed ✅\n📅 Date: {date}\n⏰ Time: {time}"

            elif not date and not time:
                return "Please provide both date and time 📅⏰"

            elif not date:
                return "Please provide the date 📅"

            elif not time:
                return "Please provide the time ⏰"

        elif intent == "greeting":
            return "Hello! How can I help you today? 😊"

        elif intent == "goodbye":
            return "Thank you! Have a great day 👋"

        else:
            return "I understood your request, but no action is defined yet."

    # 🟡 LOW confidence → use AI
    else:
        print("⚠️ Low confidence → using AI")
        return call_api(msg)