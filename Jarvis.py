import pyttsx3;
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio


engine = pyttsx3.init('sapi5');
voices = engine.getProperty('voices')
#print(voices)
engine.say("Hello I am here ");#sample code
engine.runAndWait() ;


def speak(audio):
    engine.say(audio);  # sample code
    engine.runAndWait();

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning !!!")
    elif hour>12 and hour<=18:
            speak("Good Afternoon Everone!! !!")
    else:
            speak ("Good Evening ..Hope you enjoyed your tea ")

    speak("I am your Jarvis Assistant ,Please let me know how can i ease some of your work on this phone")
def takeCommand():#it takes microphone inputs from user
   r= sr.Recognizer()#helps in recognizing audio
   with sr.Microphone() as source:
       print("Listening.....")
       r.pause_threshold = 1
      # r.energy_threshold = 100

       ## seconds of non-speaking audio before a phrase is considered complete
       audio = r.listen(source)
       print("Checking Audio")
   try:
        print("Recognizing")
        query= r.recognize_google(audio,language='en-in')
        print(f"user said:",query)
        speak(query)

   except Exception as e:
        print("Say that again  please....")
        return "None"
   return query

def sendmail(to,content):
    server =smtplib.SMTP('smtp.gmail.com',507)
    server.ehlo()
    server.starttls()
    server.login('foodpunchcafe@gmail.com','Meena@4239')
    server.sendmail('foodpunchcafe@gmail.com',to,content)
    server.close()
if __name__ == '__main__':
    wishMe()
    i=1
       # speak("what every one is doing there hope enjoy lifee !!")
    while i < 2:
        query=takeCommand().lower()#query match is easy
        #task exeute
        if 'wikipedia' in query:
            speak("Searhing Wikipedia...")
            query =query.replace("wikipedia","")
            results = wikipedia.summary(query,4)
            speak("According to  Wikipedia...")
            speak(results)

        elif 'open youtube' in query:
        #to open you tube we need to install web browser moule
         webbrowser.open("youtube.com")
        elif 'open google' in query:
         webbrowser.open("google.com")
        elif 'open facebook' in query:
        #to open you tube we need to install web browser moule
         webbrowser.open("facebook.com")

        elif 'play music' in query:
            music_dir ="C:\\Users\HP\\Desktop\\Bhajan\\hits bhajan"
            songs =os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir The time is (strtime)")
        elif 'open  code' in query:
            path = "C:\\Users\\HP\\PycharmProjects\\Desktopassistant"
            os.startfile(path)
            speak("Sir , the code is opened")
        elif 'send email' in query:
            try:
                speak("What should i send")
                content = takeCommand()
                to ="foodpunchcafe@gmail.com"
                sendmail(to,content)
                speak(f"Sir, Email has been sent ,(to)")
            except Exception as e:
                print(e)
                speak("Sorry Sir ,I am not able to sen email")

        elif 'quit' in query:
            exit()
