# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 14:46:01 2020

@author: LearnLeap
"""

from Phygital_v0 import Phygital_v0 as pyro
import time
import pygame, sys


pygame.init()

width=660
height=690

screen = pygame.display.set_mode( ( width, height) )

#Set a Title of Screen
pygame.display.set_caption('CodeReader')



pyro.pinMode('A5','dInput')
pyro.pinMode('A4','dInput')
pyro.pinMode('A3','dInput')

pyro.init("COM15")

codeDict={"000":["White Card","WhiteCard.png"],
          "001":["Light Green Card","LightGreenCard.png"],
          "010":["Yellow Card","YellowCard.png"],
          "011":["Orange Card","OrangeCard.png"],
          "100":["Blue Card","BlueCard.png"],
          "101":["Dark Green Card","DarkGreenCard.png"],
          "110":["Purple Card","PurpleCard.png"],
          "111":["No Card","NoCard.png"]}

eventstatus="none"

while True:
    pygame.display.update()
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pyro.close()
                pygame.quit()
                sys.exit()
                eventstaus="quit"
                break
            if eventstatus=="quit":
                break
            
            
        senData1=pyro.dRead('A5')
        senData2=pyro.dRead('A4')
        senData3=pyro.dRead('A3')
       
        code=str(senData1)+str(senData2)+str(senData3)
        
        print("Card Status:"+(codeDict[code][0])+" placed")
       
        path = pygame.image.load("Images/"+codeDict[code][1]).convert_alpha()
        path1=pygame.transform.scale(path,(630,660))
        screen.blit(path1,(15,15))
        time.sleep(0.1)
    except:
        if KeyboardInterrupt:
            pyro.close()
            break
        
print("Closing")
        
    

