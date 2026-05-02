import re

def extract_datetime(text):
    date = None
    time = None

    text = text.lower()

    # time detection
    time_match = re.search(r'(\d{1,2}[:.]\d{2}\s?(am|pm)?)', text)
    if time_match:
        time = time_match.group()

    # keyword dates
    if "today" in text:
        date = "today"
    elif "tomorrow" in text:
        date = "tomorrow"

    # 🔥 NEW: date format detection (dd/mm/yy)
    date_match = re.search(r'(\d{1,2}/\d{1,2}/\d{2,4})', text)
    if date_match:
        date = date_match.group()

    return date, time