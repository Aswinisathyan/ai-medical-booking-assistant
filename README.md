# 🏥 MedBook AI

### Smart Medical Booking Powered by AI

MedBook AI is an intelligent WhatsApp-based medical lab booking assistant that automates appointment scheduling and user interaction using **Machine Learning, NLP, and AI fallback mechanisms**.

---

##  Features

*  **WhatsApp Cloud API Integration** – Real-time chat-based interaction
*  **ML-Based Intent Classification** – Detects booking vs general queries
*  **NLP Response Engine** – Handles predefined and structured queries
*  **AI Fallback (LLM Integration)** – Responds to complex or unknown queries
*  **Automated Booking System** – Extracts date & time from user messages
*  **Scheduler & Reminder System** – Sends automated notifications
*  **SQLite Database** – Stores booking information
*  **Admin Dashboard** – View and manage bookings

---

##  System Workflow

User sends message via WhatsApp
↓
Intent Detection (ML Model)
↓
Decision Logic

* 📌 **Booking Request** → Entity Extraction → Store in Database
* 📌 **Known Query** → NLP Response Engine
* 📌 **Unknown Query** → AI Fallback

↓
Generate Response → Send to User

↓
Scheduler → Sends Reminder Notifications

---

##  System Architecture

* **Frontend:** WhatsApp Interface + Admin Dashboard
* **Backend:** Flask Webhook (`app.py`)
* **Processing Layer:**

  * ML Model (Intent Classification)
  * Rule Engine (Booking Logic)
  * NLP Engine (Responses)
  * AI Fallback (Groq API)
* **Database:** SQLite (`lab.db`)

---

## 🛠 Tech Stack

###  Programming & Frameworks
- **Python** – Core backend development  
- **Flask** – Web framework for webhook handling and routing  
- **HTML / CSS** – User interface for admin dashboard  

---

###  Machine Learning
- **Model Type:** Supervised Classification  
- **Algorithms:** Logistic Regression / Multinomial Naive Bayes  
- **Library:** Scikit-learn  
- **Feature Extraction:** TF-IDF Vectorizer  

---

###  Natural Language Processing (NLP)
- Text preprocessing (tokenization, normalization)  
- Rule-based and ML-assisted response generation  
- Entity extraction (date & time parsing from user input)  

---

###  AI / LLM Integration
- **Groq API (LLM)** – Handles complex or low-confidence queries  
- Provides dynamic, context-aware responses  

---

###  Database
- **SQLite** – Lightweight database for storing booking data (`lab.db`)  

---

###  APIs & Integration
- **WhatsApp Cloud API** – Enables real-time conversational interface  

---

### Scheduling & Automation
- Python-based scheduler for automated reminders and notifications  

##  Installation & Setup

```bash
git clone https://github.com/Aswinisathyan/ai-medical-booking-assistant
cd ai-medical-booking-assistant

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```


##  Run the Application

```bash
python app.py
```

---

## 📂 Project Structure

```
AI medical booking assistant/
│
├── app.py
├── router.py
├── model.py
├── api.py
├── database.py
├── scheduler.py
├── nlp_engine.py
├── entity_extractor.py
├── templates/
│   └── dashboard.html
├── requirements.txt
└── .gitignore
```

---
## screenshots
dashboard.png
whatsapp.jpeg
