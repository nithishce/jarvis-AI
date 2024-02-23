import win32com.client
import  speech_recognition as sr
import os
import webbrowser

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def say(text):
    speaker.Speak(text)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return  "Some Error Occurred. Sorry From Jarvis"
if __name__ == '__main__':
    print('PyCharm')
    say("hello i am jarvis A i")
    while True:
        print("Listening...")
        query = takeCommand()
        if "Open YouTube".lower() in query.lower():
            webbrowser.open("https://youtube.com")
            say("Opening youtube sir...")
        #say(query)



