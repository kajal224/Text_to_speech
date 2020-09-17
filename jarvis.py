import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newVoiceRate = 200
engine.setProperty('rate', newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def time():
    speak("The current time is")
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)



def date():
    Year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(Year)



def wishme():
    speak("Welcome")

    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("good morning")
    elif hour >= 12 and hour < 16:
        speak("good afternoon")
    elif hour >= 16 and hour <= 24:
        speak("good evening")
    else:
        speak("good night")

    speak("jarvis at your service. How can i help you")



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")

    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query




def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("kr04022000@gmail.com", "7858088329")
    server.sendmail("kr04022000@gmail.com", to, content)
    server.close()


def screenshot():
    img = pyautogui.screenshot()
    img.save()

def cpu():
    usage = str(psutil.cpu_percent())
    speak("cpu is at" + usage)
    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        print(query)
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            speak("going offline.")
            quit()
        elif "wikipedia" in query:
            speak("searching")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2 )
            speak(result)
        elif "send email" in query:
            try:
                speak("what should i say ?")
                content = takeCommand()
                to = "pandeypranav046@gmail.com"
                sendmail(to, content)
                speak("email sent successfully")
            except Exception as e:
                speak(e)
                speak("unable to sent the mail")
        elif "search in chrome" in query:

            speak("what should i search?")

            search = takeCommand().lower()
            
            wb.open_new_tab('https://www.google.com/?#q=' + search + ".com")
            quit()
        elif "logout" in query:
            os.system("shutdown - l")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        elif "play music" in query:
            songs = "C:\\Users\\KIIT\\Downloads\\Music"
            song = os.listdir(songs)
            os.stat(os.path.join(songs, song[0]))
        elif "remember that" in query:
            speak("what should i remember?")
            data = takeCommand()
            speak("You asked me to remember" + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()
        elif "do you remember" in query:
            remember = open("data.txt", "r")
            speak("you told me to remember that" + remember.read())
        elif "screenshot" in query:
            screenshot()
            speak("screenshot taken")
        elif "cpu" in query:
            cpu()
        elif "joke" in query:
            jokes()