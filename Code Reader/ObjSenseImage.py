# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 13:51:42 2020

@author: LearnLeap
"""

import pygame
import time
from Phygital_v0 import Phygital_v0 as pyro


# Pin Initialization
pyro.pinMode('A0','dOutput')
pyro.pinMode('A5','dInput')
#Communication Init
pyro.init("COM8")


pygame.init()

width=660
height=690

screen = pygame.display.set_mode( ( width, height) )

#Set a Title of Screen
pygame.display.set_caption('Object Sensor State')

eventstatus="none"

while True:
    pygame.display.update()
    try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pyro.close()
                    pygame.quit()
                    eventstaus="quit"
                    break
                if eventstatus=="quit":
                    break
                
            data=pyro.dRead('A5')
            
            if data==0:
                path = pygame.image.load("Images/ObjSensed.png").convert_alpha()
                path1=pygame.transform.scale(path,(630,660))
                screen.blit(path1,(15,15))
                
            else:
                path=pygame.image.load("Images/NoObj.png").convert_alpha()
                path1=pygame.transform.scale(path,(630,660))
                screen.blit(path1,(15,15))
            time.sleep(0.1)
            
    except:
            if KeyboardInterrupt:
                pyro.close()
                break
print("Closing")