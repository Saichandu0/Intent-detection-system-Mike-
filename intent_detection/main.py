import speech_recognition as sr
import pyttsx3
from training_data import training_sentences, training_labels
from intent_detector import IntentDetector

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Initialize recognizer and intent detector
recognizer = sr.Recognizer()
intent_detector = IntentDetector(training_sentences, training_labels)

def listen_and_process():
    with sr.Microphone() as source:
        speak("I'm listening...")
        try:
            # Listen for 15 seconds
            audio = recognizer.listen(source, timeout=15)
            user_input = recognizer.recognize_google(audio)
            print("You said:", user_input)
            
            # Check if input starts with trigger words
            if not (user_input.lower().startswith("hey mike") or user_input.lower().startswith("mike")):
                return
                
            # Remove trigger words from input
            user_input = user_input.lower().replace("hey mike", "").replace("mike", "").strip()
            
            # Detect intent
            intent = intent_detector.predict_intent(user_input)
            print("Detected intent:", intent)

            if intent == "unknown":
                speak("I am not able to perform that task at this moment.")
                return

            speak("Got it!")
            handle_intent(intent, user_input)
            
        except sr.WaitTimeoutError:
            return
        except sr.UnknownValueError:
            # First try - ask to repeat
            speak("Sorry, I didn't get you. Could you please repeat that?")
            try:
                # Listen again for 15 seconds
                audio = recognizer.listen(source, timeout=15)
                user_input = recognizer.recognize_google(audio)
                print("You said:", user_input)
                
                # Check if input starts with trigger words
                if not (user_input.lower().startswith("hey mike") or user_input.lower().startswith("mike")):
                    return
                    
                # Remove trigger words from input
                user_input = user_input.lower().replace("hey mike", "").replace("mike", "").strip()
                
                # Detect intent
                intent = intent_detector.predict_intent(user_input)
                print("Detected intent:", intent)

                if intent == "unknown":
                    speak("I am not able to perform that task at this moment.")
                    return

                speak("Got it!")
                handle_intent(intent, user_input)
                
            except (sr.UnknownValueError, sr.WaitTimeoutError):
                # Second try failed - terminate
                return
        except sr.RequestError:
            speak("Speech recognition service is unavailable.")
            return

def handle_intent(intent, query):
    import webbrowser
    from datetime import datetime
    import random

    if intent == "web_search" or intent == "general_knowledge":
        speak("Searching Google...")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    elif intent == "music_search":
        speak("Opening YouTube for music.")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
    elif intent == "person_lookup":
        speak(f"Looking up {query}...")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    elif intent == "get_time":
        now = datetime.now()
        time_str = now.strftime("%I:%M %p")
        date_str = now.strftime("%A, %B %d, %Y")
        speak(f"The current time is {time_str} on {date_str}")
    elif intent == "weather_query":
        speak("Let me check the weather for you.")
        webbrowser.open(f"https://www.google.com/search?q=weather")
    elif intent == "greetings":
        responses = [
            "Hello! How can I help you today?",
            "Hi there! What can I do for you?",
            "Hey! I'm here to assist you.",
            "Greetings! How may I be of service?",
            "Hello! I'm ready to help."
        ]
        speak(random.choice(responses))
    elif intent == "capabilities":
        capabilities = [
            "I can tell you the current time and date",
            "search the web for information",
            "look up people and their information",
            "help you find and play music",
            "check the weather for you",
            "answer general knowledge questions",
            "and I'm always happy to chat"
        ]
        speak("I can help you with many things! " + ", ".join(capabilities) + ".")
    else:
        speak("I'm not sure how to help with that. Could you please rephrase your request?")

if __name__ == "__main__":
    listen_and_process()
