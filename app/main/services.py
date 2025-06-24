import os
import google.generativeai as genai
from PIL import Image

try:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    print("Gemini Service: API Key configured.")
except Exception as e:
    print(f"Gemini Service: Error configuring API Key: {e}")
    raise Exception("Gemini Service: Failed to configure API key.")

def generate_story_from_image(image_file, location, tone):
    try:
        img = Image.open(image_file.stream)
        model = genai.GenerativeModel('gemini-1.5-flash')

        prompt_templates = {
            "creative": f"You are a creative travel blogger. Write a short, engaging travel story based on this image. The location is {location}. Make the story personal and vivid. Don't add a title.",
            "funny": f"You are a comedy writer. Write a hilarious story about what's happening in this image. The location is {location}. Exaggerate everything for comedic effect. Don't add a title.",
            "romantic": f"You are a romance novelist. Write a short, sweet, and romantic story inspired by this image. The location is {location}. Focus on feelings of love and connection. Don't add a title.",
            "horror": f"You are a horror writer. Look at this peaceful image and describe the unsettling thing that is just out of frame or about to happen. The location is {location}. Build suspense. Don't add a title.",
            "poetic": f"You are a poet. Write a short, beautiful poem about the moment captured in this image. The location is {location}. Focus on imagery and emotion. Don't add a title."
        }

        selected_prompt = prompt_templates.get(tone, prompt_templates["creative"])
        prompt = [selected_prompt, img]

        print("Sending request to Gemini API from service...")
        response = model.generate_content(prompt)
        print("Received response from Gemini API.")

        return response.text
    except Exception as e:
        print(f"Error in Gemini service: {e}")
        return f"An error occurred while generating the story: {str(e)}"