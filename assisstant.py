from bson import _name_value_to_bson
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import pywhatkit as kit
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning panda!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon panda!")   

    else:
        speak("Good Evening panda!")  

    speak("I am your assistant Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rudrapratapp015@gmail.com', 'rudra.panda4877')
    server.sendmail('rudrapratapp015@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'hello ' in query:
            speak ("Hello sir,how may i help you")

        elif 'open notepad' in query:
            speak("Opening Notepad")
            notepad_path = "C:\\Windows\\System32\\notepad.exe"  # Path to the Notepad executable
            os.startfile(notepad_path)
            

        elif 'what is python' in query:
            speak ("searching from google....")
            query = "what is python"
            kit.search(query)
            #webbrowser.open ("https://www.google.com/search?q=what+is+python&oq=what+is+python&gs_lcrp=EgZjaHJvbWUyDAgAEEUYORixAxiABDIKCAEQABixAxiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCTUwODJqMGoxNagCCLACAQ&sourceid=chrome&ie=UTF-8")

        elif 'open youtube' in query:
            speak ("Opening youtube")
            webbrowser.open("youtube.com")

        elif 'how algorithm coded in python' in query:
            speak ("searching")
            webbrowser.open ("https://www.google.com/search?q=how+algorithm+coded+in+python&oq=how+algorithm+coded+&gs_lcrp=EgZjaHJvbWUqBwgBECEYoAEyCQgAEEUYORifBTIHCAEQIRigATIHCAIQIRigATIHCAMQIRigATIHCAQQIRigATIHCAUQIRifBdIBCzEyMDQ4MmowajE1qAIIsAIB&sourceid=chrome&ie=UTF-8")

        elif 'play ddlj in guitar' in query:
            speak ("playing ...")
            webbrowser.open("https://www.youtube.com/shorts/-RD26JN8WkE")
            

        elif 'open google' in query:
            speak ("Opening google")
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            speak ("opening facebook")
            webbrowser.open("facebook.com")   


        elif 'play music' in query:
            speak ("playing music")
            music_dir = 'D:\song'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")


        elif 'email to rudra' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "rudrapratapp015@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")
