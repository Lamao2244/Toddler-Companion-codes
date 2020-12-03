import time
import board
import busio
import adafruit_vl53l0x

i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)


print("Initiating Sensor" , end = '\r')
time.sleep(2)

while True:
    
    if ((vl53.range/10) > 800):
    
        print("Error: Out Of Range     ",end = '\r')
        time.sleep(0.5)
        
    else:
        print("Range: {0}cm        ".format(vl53.range/10),end = '\r')
        time.sleep(0.5)

