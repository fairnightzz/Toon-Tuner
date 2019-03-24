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
        while running:
            for evt in event.get():
                if evt.type == QUIT:
                    running = False
            draw.rect(screen,(255,0,0),(100,100,400,400))
            display.flip()
        quit()

class Main:
    def __init__(self):
        settings = open("Assets/Settings.txt","r+")
        name = settings.readline()
        self.menu = Menu(name)
        settings.close()
        
        


        
main = Main()

