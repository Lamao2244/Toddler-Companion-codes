#voice recognition for Toddler companion bot! By: Adrian

#Import
import RPi.GPIO as GPIO 
import time
import os
import pygame
import speech_recognition as sr
import time
import sys
from datetime import datetime

#GPIO
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)# Red led test
GPIO.output(17,GPIO.LOW)


#init
r = sr.Recognizer()
r.energy_threshold = 4000
r.dynamic_energy_threshold = True
r.pause_threshold = 0.5




now = datetime.now()
statusmain = True
status = False     
statusb = True




#talking function
def talk(msg): 
    os.popen('espeak "' + msg + '" --stdout | aplay 2> /dev/null').read()
    
    
#Grettings function
def greet():

    day = now.strftime('%p')
    time = now.strftime('%H')
    timeact = int(time)

    if (day == 'AM'):
        talk(" Good Morning!")

    if (timeact > 12 and timeact < 18):
        talk("Good Afternoon!")
        
    if (timeact > 18):
        talk("Good Evening!")
        
#Exit music function

def exitsong():
    
    while(1):
            print("Waiting for keyword" , end = '                      \r')
            audio1 = r.listen(source  , phrase_time_limit=2)
            
            
            try:
                print("Processing..." , end ='                          \r')
                key = r.recognize_google(audio1) #google reg
                
                
                if (key == "stop"): #Keyword!!!
                    
                    pygame.mixer.music.stop()
                    time.sleep(1)
                    statusb= True
                    break
                
                    
            
            except sr.UnknownValueError:
                    pass
                
                
            except sr.RequestError as e:
                    print("Could not request results; {0}".format(e))
                    talk("There is no internet connection. Please connect to the internet.", end = '\r')
                    
def songsel():
    
      while(1):
                            
            talk("Which song would you like? , ABC  or , Baby Shark?")
            initsnd()
            audio1 = r.listen(source , phrase_time_limit=3)
            time.sleep(1)
            
            try:
                                
                opt = r.recognize_google(audio1) #google reg
                prosnd()
                time.sleep(2.0)
                print("You said:" , opt , end = '                                   \r')
                
               
                
                if(opt == "ABC"):
                        
                    talk("Playing ABC")
                    ABC()
                    exitsong()
                        
                                    
                                    
                if(opt == "baby shark"):
                        
                    talk("Playing Baby Shark")
                    shark()
                    exitsong()
                                   
                                    
            
            except sr.UnknownValueError:
                endsnd()
                time.sleep(3.0)
                print("I dont understand what you said, say again." , end = '\r')
                time.sleep(1.0)
                talk("I dont understand what you said, say again.")
                        
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
                talk("There is no internet connection. Please connect to the internet.", end = '\r')
    
   
#sound files
def initsnd():   
    pygame.mixer.init()
    pygame.mixer.music.load("init.mp3")
    pygame.mixer.music.play()

def prosnd():
    pygame.mixer.init()
    pygame.mixer.music.load("process.mp3")
    pygame.mixer.music.play()
        
def endsnd():
     pygame.mixer.init()
     pygame.mixer.music.load("end.mp3")
     pygame.mixer.music.play()

def shutdown():
     pygame.mixer.init()
     pygame.mixer.music.load("shutdown.mp3")
     pygame.mixer.music.play()
     
def ABC():
     pygame.mixer.init()
     pygame.mixer.music.load("ABC.mp3")
     pygame.mixer.music.play()
     
     
def shark():
     pygame.mixer.init()
     pygame.mixer.music.load("babyshark.mp3")
     pygame.mixer.music.play()
     
    
while(statusmain):

    with sr.Microphone() as source: #init microphone
        print("Initiating..." , end= '   \r' )
        talk("Initiating")     
        time.sleep(2.0)
        talk("System Ready!")
        print("VRS Ready" , end= '   \r' )
        time.sleep(2.0)
  
  #------------------- Keyword section --------------------
        while(statusb):
            print("Waiting for keyword" , end = '                      \r')
            audio1 = r.listen(source , phrase_time_limit=2)

            
            try:
                print("Processing..." , end ='                          \r')
                key = r.recognize_google(audio1) #google reg
               
                
                if (key == "hi" or "high"): #Keyword!!!
                    
                    statusb = False
                    status = True
            
            except sr.UnknownValueError:
                    print("Key no reg" , end ='                          \r')
                    pass
                
                
            except sr.RequestError as e:
                    print("Could not request results; {0}".format(e))
                    talk("There is no internet connection. Please connect to the internet.", end = '\r')
                
  #-------------------End of Keyword section --------------------


                                     
            while(status):  #after keyword reg
                
            
                print("Hi! What can i do for you?  Listening..." , end= '                                                   \r' )
                talk("Hi! , What can i do for you?")
                initsnd()
                audio = r.listen(source , phrase_time_limit=4)  #init microphone


                try:
                   
                    prosnd()
                    text = r.recognize_google(audio) #google reg
                    time.sleep(1)
                    print("You said:" , text , end = '                                   \r')
                    
                     #--------------------Custom commands below! --------------------
                    
                    
                    if (text == "lights on"):
                        talk("Turning on Red LED" )
                        GPIO.output(17,GPIO.HIGH)
                          
                        
                    elif (text == "lights off"):
                        talk("Turning off Red LED")
                        GPIO.output(17,GPIO.LOW)
                        
                        
                        
                    elif (text == "tell me a joke"):
                        talk("let me think of one...")
                        time.sleep(3)
                        talk("why do we tell actors to break a leg?")
                        time.sleep(1.5)
                        talk("Because every play has a CAST,  HAHAHAHAHAHAHHAHAHAHAHAHAHHAHAHAHAHAHAH")
                        time.sleep(1.5)
                        
                    elif (text == "what is the time now"):
                        
                        
                        talk("The time now is" + now.strftime('%I:%M %p') )
                        time.sleep(1.5)
                        greet()
                        
                        
                    elif (text == "bye"):
                        
                        talk("Bye Bye....")
                        time.sleep(1.5)
                        statusb = True
                        status = False
                        break
                    
                    elif (text == "play music"):
                        
                        songsel()
                        
                    else:
                    
                        talk("I think i misheard you, please repeat?")
                     
                  
                           
                    
          # ----------------------end of custom commands section ---------------------
          
          
                except sr.UnknownValueError:
                    
                    endsnd()
                    time.sleep(3.0)
                    print("I dont understand what you said, say again." , end = '\r')
                    time.sleep(1.0)
                    talk("I dont understand what you said, say again.")
                except sr.RequestError as e:
                    print("Could not request results; {0}".format(e))
                    talk("There is no internet connection. Please connect to the internet.", end = '\r')
                    



