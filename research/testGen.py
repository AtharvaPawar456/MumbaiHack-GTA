import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyD9ZF_AshNR1jYQSxdSaEED7gboME_X9_M")

model = genai.GenerativeModel(model_name="gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)