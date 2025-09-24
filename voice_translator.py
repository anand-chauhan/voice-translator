import googletrans
import speech_recognition as sr
import gtts
import playsound


# print(googletrans.LANGUAGES)
recognizer = sr.Recognizer()
text = ""  # Initialize text variable
with sr.Microphone() as source:
    print("Speak Now")
    voice = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(voice, language="hi")
        print("You said:", text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

if text:  # Proceed with translation and TTS only if text is not empty
    translator = googletrans.Translator()
    translation = translator.translate(text, dest="fr")
    print(translation.text)

    try:
        converted_audio = gtts.gTTS(translation.text, lang="fr")
        converted_audio.save("translated_speech.mp3")
        playsound.playsound("translated_speech.mp3")
    except ValueError as e:
        print(f"Error: {e}")
        # Fallback to a default language, e.g., English
        converted_audio = gtts.gTTS(translation.text, lang="fr")
        converted_audio.save("translated_speech.mp3")
        playsound.playsound("translated_speech.mp3")

