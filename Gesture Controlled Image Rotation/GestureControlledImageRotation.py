"""
Program to Rotate an image in a direction of a Gesture sensed through
two IR proximity sensors

IR Proximity Sensor1 is connected at IO pin 1 
IR Proximity Sensor2 is connected at IO pin 2 

IO Pin 1 is configured to Digital Input, to read Digital values from sensor
IO Pin 2 is configured to Digital Input, to read Digital values from sensor

"""
from Phygital_v0 import Phygital_v0 as phy
from time import sleep as s
import pygame
import rotateImage as rotator
pygame.init()


""" Set the Dimension of the Screen"""
Width = 700
Height = 640

""" Set the Screen"""
screen = pygame.display.set_mode((Width,Height))


""" Set The Title of Screen"""
pygame.display.set_caption("Sensor Based Display")

""" Load the Image"""
screenImg = pygame.image.load("Images/background.jpg")

""" Display Image at Specific Co-Ordinate"""

screen.blit(screenImg,(0,0))

img=pygame.image.load("Images/arrow.png")
newimg=pygame.transform.scale(img,(400,400))
        
screen.blit(newimg,(60,60))

phy.pinMode("A0","dinput")
phy.pinMode("A1","dinput")
phy.init("COM13")

while True:
    try:
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                phy.close()
                EventStatus="Quit"
                break
            
        
        data1=phy.dRead('A0')
        data2=phy.dRead('A1')
        if data1 == 0:
            
            while data2==1:
                print("In While")
                data2=phy.dRead("A1")
            screenImg = pygame.image.load("Images/background.jpg")
            screen.blit(screenImg,(0,0)) 
        
            img= pygame.image.load("Images/arrow.png")
               
       
            newimg=pygame.transform.scale(newimg,(400,400))
        
            for i in range (10,360,10):
                # print("in For")
                pygame.display.update()
                rotator.blitRotate(screen,newimg,(280,300),-i)
                print("in For")
                s(0.1)
            
        elif data2==0:
            while data1==1:
                data1=phy.dRead("A0")
            screenImg = pygame.image.load("Images/background.jpg")
            screen.blit(screenImg,(0,0)) 
        
            img= pygame.image.load("Images/arrow.png")
               
       
            newimg=pygame.transform.scale(img,(400,400))
        
            for i in range (10,360,10):
                pygame.display.update()
                rotator.blitRotate(screen,newimg,(280,300),i)
                s(0.1)
        
        # print(data)
        
        # # newWidth=data//8
        # # newHeight= data//8
        # angle=data1//10
        
        # # print(bright)
        # screenImg = pygame.image.load("Images/background.jpg")
        # screen.blit(screenImg,(0,0)) 
        
        # img= pygame.image.load("Images/apple.jpg")
               
        # # #Function to adjust brightness of the image
        # # img.fill((bright,bright,bright),special_flags=pygame.BLEND_RGB_ADD)
        # newimg=pygame.transform.scale(img,(400,400))
        # # screen.blit(newimg,(10,10)) 
        
        # rotator.blitRotate(screen,newimg,(280,300),-angle)
 
        # time.sleep(1)
        
    except:
        if KeyboardInterrupt:
            pygame.quit()
            phy.close()
            break
        
        
print("Closing")
