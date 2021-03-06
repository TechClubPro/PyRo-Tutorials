# -*- coding: utf-8 -*-
from Phygital_v0 import Phygital_v0 as phy
import time 

phy.init("COM8") #Add the COM Port Number Here

while True:
    try:
        print("Servo Motors in Action")
        
        phy.MoveServo(10,90)
        phy.MoveServo(11,90)
        
        time.sleep(1)
        
        phy.MoveServo(10,10)
        phy.MoveServo(11,10)
        
        time.sleep(1)
        
    except:
        if KeyboardInterrupt:
            phy.close()
            break
        
print("Closing")