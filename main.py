import speech_recognition as sr
from transformers import pipeline, Conversation
import pyttsx3

recognizer = sr.Recognizer()

engine = pyttsx3.init()

chatbot = pipeline("conversational", model="facebook/blenderbot-400M-distill")

def listen():
    with sr.Microphone() as source:
        print("Molim vas, govorite...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language="hr-HR")
            print("Prepoznat tekst: " + text)
            return text
        except sr.UnknownValueError:
            print("Nije moguće prepoznati govor")
            return None
        except sr.RequestError:
            print("Greška u prepoznavanju")
            return None

def speak(text):
    engine.say(text)
    engine.runAndWait()

def chat(text):
    conversation = Conversation(text)
    response = chatbot(conversation)
    return response.generated_responses[0]

if __name__ == "__main__":
    while True:
        user_input = listen()
        if user_input:
            bot_response = chat(user_input)
            print("Bot: " + bot_response)
            speak(bot_response)
