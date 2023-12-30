import speech_recognition as sr
import pyttsx3
from datetime import datetime
from pyowm import OWM
from pyowm.commons.exceptions import NotFoundError

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None
    except sr.WaitTimeoutError:
        print("Listening timed out. Please try again.")
        return None


def get_weather(city):
    try:
        owm = OWM('aa67a77495ddfb24fb0b96c7adc987f1')
        mgr = owm.weather_manager()
        observation = mgr.weather_at_id(1269843)
        weather = observation.weather
        temperature = weather.temperature('celsius')['temp']
        return f"The temperature in {city} is {temperature} degrees Celsius."
    except NotFoundError:
        print(f"Sorry, I couldn't find the city {city}. Please try again with a valid city name.")
        return None




def main():
    speak("Hello! How can I assist you today?")
    
    while True:
        command = get_command()

        if command:
            if "hello" in command:
                speak("Hello! How can I help you?")
            elif "time" in command:
                current_time = datetime.now().strftime("%H:%M")
                speak(f"The current time is {current_time}")
            elif "date" in command:
                current_date = datetime.now().strftime("%Y-%m-%d")
                speak(f"Today's date is {current_date}")
            elif "email" in command:
                # Implement email sending logic
                speak("Sorry, email functionality is not implemented in this example.")
            elif "weather" in command:
                city = command.split("weather in ")[-1]
                if city:
                    weather_report = get_weather(city)
                    speak(weather_report)
                else:
                    speak("Please specify a city for the weather.")
            elif "exit" in command or "bye" in command:
                speak("Goodbye! Have a great day.")
                break
            else:
                speak("Sorry, I didn't understand that command. Please try again.")

if __name__ == "__main__":
    main()
