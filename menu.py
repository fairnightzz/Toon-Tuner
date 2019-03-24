from pygame import*
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '20,30'
res=(1200,750)
screen=display.set_mode(res)
display.set_caption("Toon-Tuner")
screen.fill((0,0,0))

import tkinter
class Menu:
    def __init__(self,username):
        if username == "Guest":
            print("Change username")
            
        else:
            print("Welcome",username)
        running=True
        current = "Main"
        mainl = ["New File","Open File","Settings"]
        mainpic = [image.load("Graphics/LightNew.png"),image.load("Graphics/DarkIntro.png"),image.load("Graphics/LightIntro.png")]
        pos = [[200,100],[200,300],[200,500]]
        
        while running:
            for evt in event.get():
                if evt.type == QUIT:
                    running = False
            draw.rect(screen,(255,0,0),(100,100,400,400))
            if current == "Main":
                for i in range(len(mainpic)):
                    screen.blit(mainpic[i],(pos[i]))
            
            
            display.flip()
        quit()

class Main:
    def __init__(self):
        settings = open("Assets/Settings.txt","r+")
        name = settings.readline()
        self.menu = Menu(name)
        settings.close()
        
        


        
main = Main()

