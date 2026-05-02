from groq import Groq

#client = Groq(api_key="")

def call_api(message):
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "user", "content": message}
            ],
            model="llama-3.1-8b-instant"
        )

        return response.choices[0].message.content

    except Exception as e:
        print("❌ Groq Error:", e)
        return "AI service not available"