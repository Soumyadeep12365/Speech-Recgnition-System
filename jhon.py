import pyttsx3
import speech_recognition as sr # pip install speechRecognitio 
import datetime
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print (voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
   rr=engine.getProperty('rate')
  # print(rr)
   rr=150
   engine.setProperty('rate',rr)
   engine.say(audio)
   engine.runAndWait()
def welcome():
    h=int(datetime.datetime.now().hour)  
    if(h>=0 and h<12):
        speak("Goodmorning  Have a nice day ")
    elif(h>=12 and h <18):
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hi what can i do for you ")
def takeCommand():
    rec=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        rec.pause_threshold=.5
        audio=rec.listen(source)
    try:
       # print("Trying to Decode...")
        command=rec.recognize_google(audio,language="en-in")
        print("User Said ",command)
    except Exception as e:
        print(e)
        #speak("Unable to Recognise your command , please say it again..")
        return "NONE"
    return command
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    SUBJECT="This is a Testing Mail"
    message='Subject:{}\n\n{}'.format(SUBJECT,content)
    server.login('deepsoumya201999@gmail.com','deepsoumya1999@20')
    server.sendmail('deepsoumya201999@gmail.com',to,message)
    server.close()

if __name__=="__main__" :
    speak("welcome to the world of python programming")
    welcome()
    while True:
        q = takeCommand().lower()  
        if 'wikipedia' in q:
            speak('Searching Wikipedia...')
            q = q.replace("wikipedia", "")
            results = wikipedia.summary(q, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
  
        elif 'open youtube' in q:
            webbrowser.open("youtube.com") 
        elif 'goodbye' in q:
            speak("ok goodbye see you again")
            break  
        elif 'search' in q:
            results = wikipedia.summary(q, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'who' in q:
            results = wikipedia.summary(q, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open google' in q:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in q:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in q:
             music_dir = 'F://my music'
             songs=os.listdir(music_dir)
             #print(songs)
             os.startfile(os.path.join(music_dir, songs[5]))
        elif 'time' in q:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir the time is {strTime}")
        elif 'open vs code' in q:
            codePath ="C:\\Users\\test\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codePath)
        elif 'open whatsapp' in q:
            codePath ="C:\\Users\\test\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(codePath)
        elif 'mail' in q:
            try:
                speak("What should i say?")
                content = takeCommand()
                to="soumyadeep.rkm@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                 print(e)
                 speak("Sorry, I am not able to send this email")


        
                         
