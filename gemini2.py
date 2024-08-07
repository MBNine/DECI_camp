import google.generativeai as genai

API_KEY = "AIzaSyBzYcCOWRhjK1XrjJvoBHzOg59NJ012TZc"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(model_name='gemini-1.5-flash')
response = model.generate_content('say hello for me')

print(response.text)