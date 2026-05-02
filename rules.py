def rule_engine(intent, msg):
    if intent == "booking":
        return "Please provide date and time for your test."
    
    elif intent == "report_status":
        return "Your report will be available soon."
    
    elif intent == "cancel":
        return "Your booking has been cancelled."
    
    elif intent == "reschedule":
        return "Please provide new date and time."
    
    elif intent == "test_query":
        return "We offer CBC, Blood, Thyroid, and Diabetes tests."
    
    else:
        return "Can you please clarify your request?"