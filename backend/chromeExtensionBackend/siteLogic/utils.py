import requests

def generate_ai_quote(theme):
    api_key = "AIzaSyAP8BPbaHWMud_HT_cELTc859WP7oRNwus"
    url = "https://gemini.googleapis.com/v1/generateText"  # Adjust with the correct endpoint

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "input": {
            "text": f"Provide a motivational quote about {theme}."
        },
        "parameters": {
            "maxOutputTokens": 50,
            "temperature": 0.7
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        quote_data = response.json()
        ai_quote_text = quote_data.get('output', {}).get('text')  # Adjust based on actual response structure
        return ai_quote_text
    else:
        raise Exception("Failed to generate quote. Please check your API setup.")
 