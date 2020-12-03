from imutils import face_utils
import dlib
import cv2
from imutils.video import VideoStream
import imutils
import time
from PIL import Image
import pytesseract
import RPi.GPIO as GPIO
import time
        
#iniate GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24,GPIO.OUT) # Red led 24
GPIO.setup(23,GPIO.OUT) #green led 23
GPIO.output(23,GPIO.LOW)
GPIO.output(24,GPIO.LOW)

result = True
detector = dlib.get_frontal_face_detector()

print("-> Initating Program" , end = '\r')
c = VideoStream(src=0).start()         		    
time.sleep(2.0)


while True:

    frame = c.read()
    frame = imutils.resize(frame, width=650)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rects = detector(gray, 0)

    for rect in rects:
        x1 = rect.left()
        y1 = rect.top()
        x2 = rect.right()
        y2 = rect.bottom()
        frame = cv2.rectangle(frame, (x1,y1), (x2,y2), (255, 0, 0), 2)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
     
 
   
    cv2.imwrite("test.png",frame)
  
    img = Image.open("test.png") 
    area = (8,3,110,52) 
    crop = img.crop(area) #crops image

    img = crop
    
    temp = pytesseract.image_to_string(img, config='digits') #digit reg and convert to string
    
   
    try:
        res = float(temp)
        
        if res > 30: #Fever temperature
            print("[FEVER DETECTED!]" , res , end='\n')
            GPIO.output(24,GPIO.HIGH)
            GPIO.output(23,GPIO.LOW)
            
          
    
        else:
            print("Temperature is:", res , end='\r')
            GPIO.output(24,GPIO.LOW)
            GPIO.output(23,GPIO.HIGH)
            
            
        
    except ValueError:
            pass

    
  
            

    if key == ord("q"):
        print("-> Quiting Program...")
        time.sleep(2.0)
        break

GPIO.output(24,GPIO.LOW)
GPIO.output(23,GPIO.LOW)
cv2.destroyAllWindows()
c.stop()





