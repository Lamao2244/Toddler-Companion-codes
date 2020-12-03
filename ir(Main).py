import time
from numpy.linalg import inv
import busio
import digitalio
import board
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)# Red led
print("Initiating Sensor" , end = '\r')
time.sleep(2)

import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)
# create the mcp object
mcp = MCP.MCP3008(spi, cs)
# create an analog input channel on pin 0

while True:
    
    chan = AnalogIn(mcp, MCP.P0)
    
    v = chan.voltage
    dist = 13.91/v * 2 - 2
    distr = round(dist,1)
    
    
    if (( distr < 50) and (chan.value < 60000)) :
        print("Distance =  ", distr , "cm" )
    
    else:
        print("Out Of Range     " , end = '\r')
    
    
    if ( distr < 15): #distance trigger abt 15cm from obstacle 
          
        GPIO.output(17,GPIO.HIGH)
        
    else:
    
        GPIO.output(17,GPIO.LOW)
        

    time.sleep(1)