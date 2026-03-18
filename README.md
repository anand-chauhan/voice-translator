# 🎤 Voice Translation Project

A simple Python-based application that captures voice input, converts it to text, translates it into another language, and plays the translated speech.

---
## 🚀 Features

- 🎙️ Speech Recognition (Voice to Text)
- 🌐 Language Translation (Hindi → French)
- 🔊 Text-to-Speech Output
- ⚡ Real-time audio processing

---
## 🛠️ Tech Stack

- Python
- SpeechRecognition
- Googletrans
- gTTS (Google Text-to-Speech)
- Playsound

---

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/voice-translation-project.git
cd voice-translation-project

Install required dependencies:

pip install googletrans==4.0.0-rc1
pip install SpeechRecognition
pip install gTTS
pip install playsound
pip install pyaudio

▶️ How It Works

The program listens to your voice input via microphone.
Converts speech to text using Google Speech Recognition.
Translates the text from Hindi (hi) to French (fr).
Converts translated text into speech.
Plays the translated audio.

🧪 Usage
Run the script:
python app.py

Then:
Speak in Hindi 🎙️
The app will print the recognized text
It will translate it into French
And play the translated voice 🔊

📁 Project Structure
voice-translation-project/
│── app.py
│── translated_speech.mp3
│── README.md

⚙️ Configuration

You can change languages easily:
# Speech recognition language
recognize_google(voice, language="hi")
# Translation target language
translator.translate(text, dest="fr")
# Text-to-speech language
gTTS(translation.text, lang="fr")
