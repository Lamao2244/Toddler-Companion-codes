#voice recognition for Toddler companion bot! IP09

#Import
import RPi.GPIO as GPIO 
import time
import os
import pygame
import speech_recognition as sr
import time
import sys
import cv2
import numpy as np
from datetime import datetime
from ffpyplayer.player import MediaPlayer
from PIL import Image

#GPIO
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN, pull_up_down = GPIO.PUD_UP)


#global variable
error = 0


#init
r = sr.Recognizer()
r.energy_threshold = 4000
r.dynamic_energy_threshold = True
r.pause_threshold = 0.5
now = datetime.now()

#button function
def button():
    
        input_state = GPIO.input(18)
        if input_state == False:
            print("Stop button pressed")
            active()
  
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
        
def blank():
    
    display_width = 1920
    display_height = 1080

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    Img = pygame.image.load('blank.jpg')
    
def A():
   
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    filename = ('A.jpg')
    img = pygame.image.load(filename)
    screen.blit(img, (0, 0))
    pygame.display.flip()

 
    
def B():
    
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    filename = ('B.jpg')
    img = pygame.image.load(filename)
    screen.blit(img, (0, 0))
    pygame.display.flip()

    
    
#guess the letter game
            
def game():        
    
    talk("loading, name the object game.....")
    time.sleep(3)
    talk("How to play? Name the object that is being displayed! You dont have a time limit!")
    time.sleep(1)
    game1()


def game1():
    
    while(1):
            pygame.quit()
            A()
            talk("Name the object than is shown! Say , quit ,to go back to main menu")        
            initsnd()
            audio1 = r.listen(source , phrase_time_limit= 2)
            time.sleep(1)
            
            try:
                                
                ans1 = r.recognize_google(audio1) #google reg
                prosnd()
                time.sleep(2.0)
                print("You said:" , ans1 , end = '                                   \r')
                
               
                
                if(ans1 == "apple"):
                        
                    talk("Well done, You got it correct")
                    time.sleep(2)
                    talk("lets move on to the next one!")
                    pygame.quit()
                    game2()
                    
                if(ans1 == "Apple"):
                        
                    talk("Well done, You got it correct")
                    time.sleep(2)
                    talk("lets move on to the next one!")
                    pygame.quit()
                    game2()



                elif(ans1 == "quit"):
                    
                    cv2.destroyAllWindows()
                    active()
    
                else:
                    talk("Sorry,your answer is incorrect! Or i misheard you? try again!")   
                   
                                  
            
            except sr.UnknownValueError:
                endsnd()
                time.sleep(3.0)
                print("I dont understand what you said, say again." , end = '\r')
                time.sleep(1.0)
                talk("I dont understand what you said, say again.")
                        
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
                talk("There is no internet connection. Please connect to the internet.", end = '\r')

def game2():
    
        while(1):
            
            talk("What is the object shown?")
            B()
            initsnd()
            audio1 = r.listen(source , phrase_time_limit=2)
            time.sleep(1)
            
            try:
                                
                ans2 = r.recognize_google(audio1) #google reg
                prosnd()
                time.sleep(2.0)
                print("You said:" , ans2 , end = '                                   \r')
                
               
                
                if(ans2 == "Ball"):
                        
                    talk("Well done! You got it correct")
                    time.sleep(2)
                    talk("You won all the stages Well done, returning to main menu" )
                    pygame.quit()
                    active()
                    
                elif(ans2 == "ball"):
                        
                    talk("Well done! You got it correct")
                    time.sleep(2)
                    talk("You won all the stages Well done, returning to main menu" )
                    pygame.quit()
                    active()
                    


                elif(ans2 == "quit"):
                     
                    pygame.quit()
                    active()
    
                else:
                    talk("Sorry,your answer is incorrect! Or i misheard you? try again!")   
                   
                                  
            
            except sr.UnknownValueError:
                endsnd()
                time.sleep(3.0)
                print("I dont understand what you said, say again." , end = '\r')
                time.sleep(1.0)
                talk("I dont understand what you said, say again.")
                        
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
                talk("There is no internet connection. Please connect to the internet.", end = '\r')


def selmusic():

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
                                       
                                                                        
                                                                                    
                                                        
            elif(opt == "baby shark"):
                                            
                talk("Playing Baby Shark")
                shark()
                exitsong()
                
            else:
                talk("Sorry, that song is not in my library yet, or i misheard what you said? ,Say again?")
                        
                                          
                                                        
                                
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
     
def getVideoSource(source, width, height):
    cap = cv2.VideoCapture(source)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    return cap

def pig():
    
    pygame.quit()
    sourcePath = "pig.mp4"
    camera = getVideoSource(sourcePath, 1920, 1080)
    player = MediaPlayer(sourcePath)

    while True:
            
        ret, frame = camera.read()
        audio_frame, val = player.get_frame()

        if (ret == 0):
            print("End of video")
            cv2.destroyAllWindows()
            blank()
            break

        frame = cv2.resize(frame, (1920, 1080))
        cv2.imshow('Camera', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            camera.release()
            cv2.destroyAllWindows()
            blank()
            break
            
            
        if GPIO.input(18) == False:
            
            camera.release()
            cv2.destroyAllWindows()
            blank()
            break
            
        if val != 'eof' and audio_frame is not None:
            frame, t = audio_frame
            
      
           


if __name__ == "__pig__":
    pig()



def bean():
    
    pygame.quit()
    sourcePath = "bean.mp4"
    camera = getVideoSource(sourcePath, 1920, 1080)
    player = MediaPlayer(sourcePath)

    while True:
            
        ret, frame = camera.read()
        audio_frame, val = player.get_frame()

        if (ret == 0):
            print("End of video")
            cv2.destroyAllWindows() 
            break

        frame = cv2.resize(frame, (1920, 1080))
        cv2.imshow('Camera', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            camera.release()
            cv2.destroyAllWindows()
            break
            
            
        if GPIO.input(18) == False:
            
            camera.release()
            cv2.destroyAllWindows()
            blank()
            break
               
               
        if val != 'eof' and audio_frame is not None:
            frame, t = audio_frame
          
    

if __name__ == "__bean__":
    bean()
    

            
            
            
def exitsong():

    while(1): 
        
        if GPIO.input(18) == False:
            
               active()
           
        time.sleep(0.2)
                    
    
#idle function
def idle():


  
    status = False     
    statusb = True

    while(True):

           
            time.sleep(2.0)
            talk("Idling...")
            print("VRS Ready" , end= '   \r' )
            blank()
            time.sleep(2.0)
      
      #------------------- Keyword section --------------------
            while(statusb):
                print("Waiting for keyword" , end = '                      \r')
                audio1 = r.listen(source , phrase_time_limit=2)

                
                try:
                    print("Processing..." , end ='                          \r')
                    key = r.recognize_google(audio1) #google reg
                   
                    
                    if (key == 'hi'): #Keyword!!!
                        
                        active()
                        
                    if (key == 'high'): #Keyword!!!
                        
                        active()
                        
                    if (key == 'hello'): #Keyword!!!
                        
                        active()
                        
                except sr.UnknownValueError:
                        print("Key no reg" , end ='                          \r')
                        pass
                    
                    
                except sr.RequestError as e:
                        print("Could not request results; {0}".format(e))
                        talk("There is no internet connection. Please connect to the internet.", end = '\r')
                    
      #-------------------End of Keyword section --------------------

#active function
def active():

   
                blank()
                while(True):  
                    
                     
                    print("Hi! What can i do for you?  Listening..." , end= '                                                   \r' )
                    talk("What can i do for you?")
                    initsnd()
                    audio = r.listen(source , phrase_time_limit=4)  #init microphone


                    try:
                       
                        prosnd()
                        text = r.recognize_google(audio) #google reg
                        time.sleep(1)
                        print("You said:" , text , end = '                                   \r')
                        
                         #--------------------Custom commands below! --------------------
                            
                            
                        if (text == "tell me a joke"):
                            talk("let me think of one...")
                            time.sleep(3)
                            talk("why do we tell actors to break a leg?")
                            time.sleep(1.5)
                            talk("Because every play has a CAST,  HAHAHAHAHAHAHHA")
                            time.sleep(1.5)
                            
                        elif (text == "what is the time now"):
                            
                            
                            talk("The time now is" + now.strftime('%I:%M %p') )
                            time.sleep(1.5)
                            greet()
                            
                            
                        elif (text == "bye"):
                            
                            talk("going to idle, Bye Bye....")
                            time.sleep(1.5)
                            idle()
                        
                        elif (text == "bye-bye"):
                            
                            talk("going to idle, Bye Bye....")
                            time.sleep(1.5)
                            idle()
                        
                        elif (text == "play music"):
                            
                            selmusic()
                                         
                        elif (text == "play video"):
                            
                            talk('loading video...')
                            time.sleep(1)
                            pig()
                            
                        elif(text == "play game"):
                            game()
                            
                        elif(text == "play Gabe"):
                            game()
                            
                        elif(text == "play date"):
                            game()
                            
                        elif(text == "play gate"):
                            game()
                            
                        elif(text == "play babe"):
                            game()
                          
                          
                        #-----Motor Voice commands------
                            
                        elif(text == "forward"):
                            
                            talk("Moving Forward.")
                            
                            #Forward motor function
                            
                        elif(text == "backwards"):
                            
                            talk("Moving backwards.")
                            
                            #reverse motor function
                            
                        elif(text == "left"):
                            
                            talk("Moving left.")
                            
                            #left motor function
                            
                        elif(text == "right"):
                            
                            talk("Moving right.")
                            
                            #right motor function
                            
                        elif(text == "stop"):
                            
                            talk("Stopping robot")
                            
                            #stop motor function
                            
                            
                        elif(text == "auto"):
                            
                            talk("auto mode enabled")
                            
                            #auto tracking mode function
                            
                            
                        elif(text == "manual"):
                            
                            talk("Manual mode enabled")
                            
                            #manual mode function
                            
                        else:
                            talk("Sorry, that is not something i can do yet, or i misheard what you said? ,Say again?")
                        
              # ----------------------end of custom commands section ---------------------
              
                        
                    except sr.UnknownValueError:
                        
                        endsnd()
                        
                        global error
                        error = error + 1
                        
                        if (error == 4):
                            talk("Going to idle....")
                            time.sleep(1)
                            idle()
                        
                        else:
                            time.sleep(3.0)
                            print("I dont understand what you said, say again." , end = '\r')
                            time.sleep(1.0)
                            talk("I dont understand what you said, say again.")
                            
                    except sr.RequestError as e:
                        print("Could not request results; {0}".format(e))
                        talk("There is no internet connection. Please connect to the internet.", end = '\r')
 

while(1):

    with sr.Microphone() as source: #init microphone
        idle()


