from __future__ import with_statement 
import pyttsx3  
import speech_recognition as sr  
import datetime 
import wikipedia 
import webbrowser 
import os 
import random 
import cv2 
import pywhatkit as kit 
import sys 
import pyautogui 
import time 
import operator 
import requests
import turtle
import numpy as np  

engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id) 
engine.setProperty('rate', 150)


def speak(audio):
  engine.say(audio) 
  engine.runAndWait()
  
def wishMe(): 
  hour = int(datetime.datetime.now().hour) 
  if hour>=0 and hour<12: 
    speak("Good Morning!") 
  elif hour>=12 and hour<18: 
    speak("Good Afternoon!")    
  else: 
    speak("Good Evening!")
    
def takeCommand(): 
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
    print("Say that again please...")   
    return "None" 
  return query


def Pass(pass_inp):

    password = "admin"

    passss  = str(password)

    if passss==str(pass_inp):

        speak("Access Granted .")

        speak("Initializing Jarvis")

             
        speak("Starting all systems applications")
             
        speak("Installing and checking all drivers")
         
        speak("Caliberating and examining all the core processors")
             
        speak("Checking the internet connection")
             
        speak("Wait a moment sir")
             
        speak("All drivers are up and running")
             
        speak("All systems have been activated")
             
        speak("Now I am online")
             
        print("Initializing Jarvis")
             
        print("Starting all systems applications")
             
        print("Installing and checking all drivers")
             
        print("Caliberating and examining all the core processors")
             
        print("Checking the internet connection")
             
        print("Wait a moment sir")
             
        print("All drivers are up and running")
             
        print("All systems have been activated")
             
        print("Now I am online")

        speak("i am jarvis sir, online and ready to help you sir")
              

             



        import main 

    else:
             
        speak("Access Not Granted .")



if __name__== "__main__" :
    speak("i am  Password Protected i can only unlocked by you .")
    speak("Kindly Provide The Password To Access .")
    passssssss = takeCommand()
    Pass(passssssss)
    wishMe() 
    while True: 
        query = takeCommand().lower() 
    
        if "channel analytics" in query: 
            webbrowser.open("https://studio.youtube.com/channel/UCxeYbp9rU_HuIwVcuHvK0pw/analytics/tab-overview/period-default") 

        elif 'open youtube' in query: 
            speak("what you will like to watch ?") 
            qrry = takeCommand().lower() 
            kit.playonyt(f"{qrry}") 
    
        elif 'close chrome' in query: 
            os.system("taskkill /f /im chrome.exe") 
    
        elif 'close youtube' in query: 
            os.system("taskkill /f /im msedge.exe") 
    
        elif 'open google' in query: 
            speak("what should I search ?") 
            qry = takeCommand().lower() 
            webbrowser.open(f"{qry}") 
            results = wikipedia.summary(qry, sentences=2) 
            speak(results) 
        
        elif 'close google' in query: 
            os.system("taskkill /f /im msedge.exe") 
    
        elif 'play music' in query: 
            music_dir = 'C:\\Users\\shubh\\Music' 
            songs = os.listdir(music_dir)     
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif 'close music' in query: 
            os.system("taskkill /f /wmplayer.exe") 

        elif 'the time' in query: 
            strTime = datetime.datetime.now().strftime("%H:%M:%S")     
            speak(f"Sir, the time is {strTime}") 

        elif "shut down the system" in query: 
            os.system("shutdown /s /t 5") 
    
        elif "restart the system" in query: 
            os.system("shutdown /r /t 5") 
    
        elif "Lock the system" in query: 
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0") 
    
        elif "open notepad" in query: 
            npath = "C:\\WINDOWS\\system32\\notepad.exe"     
            os.startfile(npath) 
    
        elif "close notepad" in query: 
            os.system("taskkill /f /im notepad.exe") 

        elif "open command prompt" in query: 
            os.system("start cmd") 
    
        elif "close command prompt" in query: 
            os.system("taskkill /f /im cmd.exe")

        elif "go to sleep" in query: 
            speak(' alright then, I am switching off') 
            sys.exit() 

        elif "take screenshot" in query: 
            speak('tell me a name for the file') 
            name = takeCommand().lower() 
            time.sleep(3) 
            img = pyautogui.screenshot()   
            img.save(f"{name}.png")   
            speak("screenshot saved") 
    
        elif "calculate" in query: 
            r = sr.Recognizer() 
            with sr.Microphone() as source: 
                speak("ready") 
                print("Listning...") 
                r.adjust_for_ambient_noise(source) 
                audio = r.listen(source) 
                my_string=r.recognize_google(audio) 
                print(my_string)

            def get_operator_fn(op): 
                return { 
                '+' : operator.add, 
                '-' : operator.sub, 
                'x' : operator.mul, 
                'divided' : operator.truediv, 
                }[op] 
      
            def eval_bianary_expr(op1,oper, op2): 
                op1,op2 = int(op1), int(op2) 
                return get_operator_fn(oper)(op1, op2) 
            speak("your result is") 
            speak(eval_bianary_expr(*(my_string.split())))

        elif "what is my ip address" in query: 
            speak("Checking")
      
            try: 
                ipAdd = requests.get('https://api.ipify.org').text 
                print(ipAdd) 
                speak("your ip adress is") 
                speak(ipAdd) 
      
            except Exception as e: 
                speak("network is weak, please try again some time later")

        elif "volume up" in query: 
            pyautogui.press("volumeup") 
            pyautogui.press("volumeup") 
            pyautogui.press("volumeup") 
            pyautogui.press("volumeup") 
            pyautogui.press("volumeup") 
            pyautogui.press("volumeup") 
            pyautogui.press("volumeup") 
            pyautogui.press("volumeup") 
            pyautogui.press("volumeup") 
            pyautogui.press("volumeup") 
            pyautogui.press("volumeup") 
            pyautogui.press("volumeup") 
            pyautogui.press("volumeup") 
            pyautogui.press("volumeup") 
            pyautogui.press("volumeup") 
            
        elif "volume down" in query: 
            pyautogui.press("volumedown") 
            pyautogui.press("volumedown") 
            pyautogui.press("volumedown") 
            pyautogui.press("volumedown") 
            pyautogui.press("volumedown") 
            pyautogui.press("volumedown") 
            pyautogui.press("volumedown") 
            pyautogui.press("volumedown") 
            pyautogui.press("volumedown") 
            pyautogui.press("volumedown") 
            pyautogui.press("volumedown") 
            pyautogui.press("volumedown") 
            pyautogui.press("volumedown")  
            pyautogui.press("volumedown") 
            pyautogui.press("volumedown") 
            
        elif "mute" in query: 
            pyautogui.press("volumemute") 
    
        elif "refresh" in query: 
            pyautogui.moveTo(1551,551, 2) 
            pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right') 
            pyautogui.moveTo(1620,667, 1) 
            pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left') 
            
        elif "scroll down" in query: 
            pyautogui.scroll(1000) 
    
        elif "drag visual studio to the right" in query: 
            pyautogui.moveTo(46, 31, 2) 
            pyautogui.dragRel(1857, 31, 2) 

        elif "rectangular spiral" in query: 
            pyautogui.hotkey('win') 
            time.sleep(1) 
            pyautogui.write('paint') 
            time.sleep(1) 
            pyautogui.press('enter') 
            pyautogui.moveTo(100, 193, 1) 
            pyautogui.rightClick 
            pyautogui.click() 
            distance = 300
            while distance > 0: 
                pyautogui.dragRel(distance, 0, 0.1, button="left") 
                distance = distance - 10 
                pyautogui.dragRel(0, distance, 0.1, button="left") 
                pyautogui.dragRel(-distance, 0, 0.1, button="left") 
                distance = distance - 10 
                pyautogui.dragRel(0, -distance, 0.1, button="left")

        elif "close paint" in query: 
            os.system("taskkill /f /im mspaint.exe") 
    
        elif "hu r u" in query: 
            print('My Name Is jarvis') 

            speak('My Name Is jarvis') 
            print('I can Do Everything that my creator programmed me to do') 
            speak('I can Do Everything that my creator programmed me to do') 
    
        elif "who created you" in query: 
            print('I Do not Know His Name, I created with Python Language, in Visual Studio Code.') 
            speak('I Do not Know His Name, I created with Python Language, in Visual Studio Code.') 

        elif "open notepad and write my channel name" in query: 
            pyautogui.hotkey('win') 
            time.sleep(1) 
            pyautogui.write('notepad') 
            time.sleep(1) 
            pyautogui.press('enter') 
            time.sleep(1) 
            pyautogui.write("How To Manual", interval = 0.1) 
            
        elif "subscribe" in query: 
            print("Everyone Who are watching This, Please Subscribe Our Channel  for Interesting tutorials and information, Thanks For Watching") 
            speak("Everyone Who are watching This, Please Subscribe Our Channel  for Interesting tutorials and information, Thanks For Watching") 

        elif 'type' in query: 
            query = query.replace("type", "") 
            pyautogui.write(f"{query}")

        elif 'maximize this window' in query: 
            pyautogui.hotkey('alt', 'space') 
            time.sleep(1) 
            pyautogui.press('x') 
        
        elif 'google search' in query: 
            query = query.replace("google search", "") 
            pyautogui.hotkey('alt', 'd') 
            pyautogui.write(f"{query}", 0.1) 
            pyautogui.press('enter')

        elif 'minimise this window' in query: 
            pyautogui.hotkey('alt', 'space') 
            time.sleep(1) 
            pyautogui.press('n')
            
        elif 'open chrome' in query: 
            os.startfile('C:\\Program Files\\Google\Chrome\\Application\\chrome.exe')

        elif 'open new window' in query: 
            pyautogui.hotkey('ctrl', 'n') 

        elif 'open incognito window' in query: 
            pyautogui.hotkey('ctrl', 'shift', 'n')
            
        elif 'open history' in query: 
            pyautogui.hotkey('ctrl', 'h') 
        elif 'open downloads' in query: 
            pyautogui.hotkey('ctrl', 'j') 
        elif 'previous tab' in query: 
            pyautogui.hotkey('ctrl', 'shift', 'tab') 
        elif 'next tab' in query: 
            pyautogui.hotkey('ctrl', 'tab') 
        elif 'close tab' in query: 
            pyautogui.hotkey('ctrl', 'w')

        elif 'close window' in query: 
            pyautogui.hotkey('ctrl', 'shift', 'w') 
        elif 'clear browsing history' in query: 
            pyautogui.hotkey('ctrl', 'shift', 'delete')
            
        
        elif 'draw rectangle' in query:
            speak("here we go sir")
            img = np.zeros((400, 400, 3), dtype = "uint8") 
            cv2.rectangle(img, (30, 30), (300, 200), (0, 255, 0), 5) 

            cv2.imshow('dark', img) 

        elif 'draw circle' in query:
            speak("here we go sir")
            img = np.zeros((400, 400, 3), dtype = "uint8")  
            cv2.circle(img, (200, 200), 80, (255, 0, 2), 3) 
  
            cv2.imshow('dark', img) 
        elif 'draw square' in query:
            screen = turtle.Screen()
            screen.bgcolor("white")
            pen = turtle.Turtle()
            pen.speed(1)  
            for _ in range(4):
                pen.forward(100)
                pen.left(90)
            turtle.done()

        elif 'make some animations' in query:
            speak ("alright lets do it ")
            import pygame
            import sys      
            pygame.init()

            screen = pygame.display.set_mode((400, 300))
            pygame.display.set_caption("Simple Animation")
            black = (0, 0, 0)
            white = (255, 255, 255)

            x = 0 
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                screen.fill(white)
                pygame.draw.rect(screen, black, (x, 150, 50, 50))
                x += 1 
                pygame.display.flip()
                pygame.time.Clock().tick(60)
            pygame.quit()
            sys.exit()

        elif 'schedule whatsapp message' in query:
            speak("okay sir")
            import pywhatkit as pwk

            message = "Hello, this is a scheduled message using PyWhatKit!"
            phone_number = "+918867462853"
            hour =5
            minute = 56

            try:
                pwk.sendwhatmsg(phone_number, message, hour, minute)
                print(f"Message scheduled to be sent to {phone_number} at {hour}:{minute} successfully!")
            except Exception as e:
                print(f"An error occurred: {e}")

            speak("scheduled message at your desired time sir")

        elif 'send whatsapp message' in query:
           speak("Okay sir, sending messages")
           import pywhatkit
           import pyautogui
           import time

    
           phone_numbers = ["", "", ""]
           message = "Howdy! This message will be sent instantly!"

   
           for phone_no in phone_numbers:
              try:
               pywhatkit.sendwhatmsg_instantly(phone_no=phone_no, message=message)
               time.sleep(2)  
               pyautogui.press('enter')  
               time.sleep(2)  
               speak(f"Message sent successfully to {phone_no}")
              except Exception as e:
               speak(f"Failed to send message to {phone_no}. Error: {str(e)}")

               speak("All messages sent successfully, sir")



        elif "stop execution" in query or "exit" in query:
           speak("Alright, stopping the execution. Goodbye, sir!")
           sys.exit()