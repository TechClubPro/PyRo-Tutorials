"""
Code to Control LED State On-Off

LED connected at A0

"""

"""Library"""
from Phygital_v0 import Phygital_v0 as pyro
import time

"""Pin Initialization"""
pyro.pinMode('A0','dOutput')
pyro.pinMode('A1','dOutput')
pyro.pinMode('A2','dOutput')
pyro.pinMode('A3','dOutput')
pyro.pinMode('A4','dOutput')

"""Init"""
pyro.init("COM15")

"""LED ON"""
LEDPins=['A0','A1','A2','A3','A4']

BinaryNum={0:[0,0,0,0,0],
           1:[0,0,0,0,1],
           2:[0,0,0,1,0],
           3:[0,0,0,1,1],
           4:[0,0,1,0,0],
           5:[0,0,1,0,1],
           6:[0,0,1,1,0],
           7:[0,0,1,1,1],
           8:[0,1,0,0,0],
           9:[0,1,0,0,1],
           10:[0,1,0,1,0],
           11:[0,1,0,1,1],
           12:[0,1,1,0,0],
           13:[0,1,1,0,1],
           14:[0,1,1,1,0],
           15:[0,1,1,1,1],
           16:[1,0,0,0,0],
           17:[1,0,0,0,1],
           18:[1,0,0,1,0],
           19:[1,0,0,1,1],
           20:[1,0,1,0,0],
           21:[1,0,1,0,1],
           22:[1,0,1,1,0],
           23:[1,0,1,1,1],
           24:[1,1,0,0,0],
           25:[1,1,0,0,1],
           26:[1,1,0,1,0],
           27:[1,1,0,1,1],
           28:[1,1,1,0,0],
           29:[1,1,1,0,1],
           30:[1,1,1,1,0],
           31:[1,1,1,1,1]
           }

while True:
    try:
        
        num=int(input("Tell the Num to be converted in Binary?  "))
        
        if num>=32:
            print("") 
            print("System is 5 Bit, can only show numbers from 0-31")
            pyro.close()
            break
            
        else:
            for i in range(4,-1,-1):
                pyro.dWrite(LEDPins[i],BinaryNum[num][4-i])
        
    except:
        if KeyboardInterrupt:
            pyro.close()
            break
print("")        
print("Closed the Connection!!")

"""Closing"""
