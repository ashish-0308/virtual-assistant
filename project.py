import pyttsx3 #used for text to speech coversion by pip install pyttsx3
import speech_recognition as sr #used for voice recognition by pip install speechRecognition
import datetime
import wikipedia #used for search in wikipedia
import webbrowser #used for search engines
import os 

engine = pyttsx3.init('sapi5') #sapi5 provide voices for windows
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #for different voices in the system
engine.setProperty('rate',180) # for the assistant voice speed


def speak(audio): # for voice detection
    engine.say(audio)
    engine.runAndWait()


def wishMe(): #wishes according to time 
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir!")
        

    elif hour>=12 and hour<18:
        speak("Good afternoon sir!")
        

    else:
        speak("Good evening sir!")
          

    speak("Hope you are doing well.  I am your jin. Please tell me how may I help you") 
    

def takeCommand(): #function for taking command from the user
 

    r = sr.Recognizer() #recognizes users voice
    with sr.Microphone() as source: #microphone uses user's voice as source
        r.adjust_for_ambient_noise(source=source)
        print("Listening...")
        r.pause_threshold = 1 #for the pause between users command
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') # for recognizing what user said and in which language
        print(f"User said: {query}\n") #prints what user said

    except Exception as e: # if it doesn't recognizes the command properly
        speak("Say that again please...")
        print("Say that again please...")  
        return "None"
    return query


if _name_ == "_main_":
    wishMe()
    while True:
    
        query = takeCommand().lower()

        

        if 'my name' in query: #tells my name
            speak(' Sir, your name is Aashish Poonia')

        elif 'my age' in query: #tells my age
            birth_year = int(2000)
            birth_month = int(9)
            birth_day = int(8)
 
            current_year = datetime.date.today().year
            current_month = datetime.date.today().month
            current_day = datetime.date.today().day
 
            age_year = current_year - birth_year
            age_month = abs(current_month-birth_month)
            age_day = abs(current_day-birth_day)

            age = age_year, age_month, age_day
            print(f"Your age is: {age_year} years {age_month} months {age_day} days")
            speak(f"Your age is: {age_year} years {age_month} months {age_day} days")
        
        elif 'live' in query: #tells my address
            speak("Flat Number 7, Second Floor, Block k2, Vatika India Next, Sector 83, Gurugram, Haryana")


        elif 'wikipedia' in query: #search anything on wikipedia
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query: #opens youtube in the browser
            speak('opening youtube')
            print('opening youtube')
            webbrowser.open("youtube.com")

        elif 'open google' in query: #opens google
            speak('opening google')
            print('opening google')
            webbrowser.open("google.com") 


        elif 'the time' in query: #teels the current time
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")

        
        elif 'open command prompt' in query: #opens command propmt
            speak('opening command promt')
            print('opening command prompt')
            os.system("start cad")

       
        elif "that's it" in query: # when exits the assistant
            speak('Thank you sir. Call me whenever you need help')import pyttsx3 
