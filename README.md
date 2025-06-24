# TripTeller 📸✈️

**Turn your travel memories into vivid, shareable stories — powered by Google Gemini and your uploaded photo. Just pick a location, choose a tone, and let the AI do the magic.**
> [🔗 Watch it on YouTube]()

## ✨ Features

- **🧠 AI-Powered Storytelling:** Uses Google Gemini 1.5 Flash to generate personalized, location-aware stories from user-uploaded travel photos.
- **🎭 Multi-Tone Output:** Choose from 5 storytelling styles — *Creative*, *Funny*, *Romantic*, *Horror*, or *Poetic* — to match your vibe.
- **📷 Vision + Language Integration:** The AI interprets visual elements from uploaded images and incorporates them into the story.
- **📋 Copy to Clipboard:** One-click copy button makes sharing your story effortless.
- **📱 Responsive UI:** Built with Tailwind CSS, works seamlessly on desktop and mobile.

## 🛠️ Tech Stack
| Layer      | Technology |
|------------|------------|
| Backend    | Python, Flask |
| AI Engine  | Google Gemini 1.5 Flash (via `google-generativeai`) |
| Frontend   | HTML5, Tailwind CSS, JavaScript |
| Image      | PIL (Pillow) |
| Deployment | Localhost (Flask Dev Server) |

## 🚀 Local Development Setup
Run the app locally in just a few steps:

1. **Clone the repository**
   ```bash
   git clone https://github.com/RozhakDev/TripTeller.git
   cd TripTeller
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your API key to `.env`**
   Create a `.env` file in the root directory:
   ```
   GOOGLE_API_KEY="your_gemini_api_key_here"
   ```

5. **Run the application**
   ```bash
   python3 run.py
   ```

6. **Open in browser**
   Go to [http://localhost:5000](http://localhost:5000)

## 📸 Screenshot
![TripTeller UI](https://github.com/user-attachments/assets/4a1724f0-2493-44ee-b8be-f33bbd30cca0)

## 🏆 Why It Stands Out
- Combines LLM + Vision for **deeply contextual generation**
- Fully dynamic tone-based storytelling
- Developer-friendly structure, clean UI, and focused UX

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

## 📜 License
> MIT License © 2025 Rozhak Dev
