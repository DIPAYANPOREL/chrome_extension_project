from django.http import HttpResponse
from google.generativeai import GenerativeModel
from datetime import datetime
from django.conf import settings

# Initialize the model with your API key
model = GenerativeModel(model_name='gemini-1.5-flash')  # Specify the model you want to use

def generate_motivational_quote(theme="motivation"):
    date_str = datetime.now().strftime("%A, %B %d")
    prompt = f"Provide a motivational quote for {date_str} with a theme of {theme}."

    try:
        # Generate content using the generative AI model
        response = model.generate_content(prompt)

        # Extract the generated text from the response
        ai_quote_text = response.text
        return HttpResponse(ai_quote_text.strip() if ai_quote_text else "No quote generated.")

    except Exception as e:
        print("Error generating quote:", str(e))
        return HttpResponse("Failed to generate quote. Please check your API setup.", status=500)

# Example usage
if __name__ == "__main__":
    quote = generate_motivational_quote()
    print("Generated Quote:", quote)

