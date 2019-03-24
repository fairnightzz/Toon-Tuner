from pygame import*
import os
from tkinter import filedialog
from tkinter import*
import download
from Btn import*
os.environ['SDL_VIDEO_WINDOW_POS'] = '20,30'
res=(1200,750)
screen=display.set_mode(res)
display.set_caption("Toon-Tuner")
screen.fill((0,0,0))
class Menu:
    def __init__(self,username):
        if username == "Guest":
            print("Change username")
            
        else:
            print("Welcome",username)
        running=True
        current = "Main"
        mainl = ["New File","Open File","Settings"]
        mainpic = [Btn(image.load("Graphics/LightNew.png"),image.load("Graphics/LightNew#.png"),200,100)\
                   ,Btn(image.load("Graphics/LightOpen.png"),image.load("Graphics/LightOpen#.png"),\
                           200,300),Btn(image.load("Graphics/LightSettings.png"),image.load("Graphics/LightSettings#.png"),200,500)]
        pos = [[200,100],[200,300],[200,500]]
        #178,100
        
        mx,my = mouse.get_pos()
        while running:
            mx,my = mouse.get_pos()
            for evt in event.get():
                if evt.type == QUIT:
                    running = False
            #draw.rect(screen,(255,0,0),(100,100,400,400))
                if evt.type == MOUSEBUTTONDOWN:
                    if current == "Main":
                        for n in range(len(mainpic)):
                            if Rect(mainpic[n].rect[0],mainpic[n].rect[1],178,100).collidepoint(mx,my):
                                #current = mainl[n]
                                print(mainl[n])
                                mainpic[n].pressed = True
                                #dialog = self.newFile("Enter File Name")
                if evt.type == MOUSEBUTTONUP:
                    if current == "Main":
                        for n in range(len(mainpic)):
                            mainpic[n].pressed = False
                        for n in range(len(mainpic)):
                            if Rect(mainpic[n].rect[0],mainpic[n].rect[1],178,100).collidepoint(mx,my):
                                current = mainl[n]
                                if current == mainl[0]:
                                    dialog = self.newFile("Enter File Name")
            screen.fill((0,0,0))
            if current == "Main":
                for i in range(len(mainpic)):
                    mainpic[i].draw(screen)
            elif current == "New File":
                print("new file")
            elif current == "Open File":
                print("open file")
            elif current == "Settings":
                print("settings")
            display.flip()
        quit()

    def newFile(self,message):
        test = takeInput(message)
        test.mainloop()
        message = test.returnmessage()
        download.create_folder("User Files/%s/"%(message))
        return message
        


class takeInput(Tk):
    def __init__(self,message):
        Tk.__init__(self)
        self.entry = Entry(self)
        self.button = Button(self, text=message, command=self.on_button)
        self.entry.pack()
        self.button.pack()
        self.message = ""

    def on_button(self):
        self.message = (self.entry.get())
        self.destroy()
        
        
        #self.destroy()
    def returnmessage(self):
        return self.message

class Main:
    def __init__(self):
        settings = open("Assets/Settings.txt","r+")
        name = settings.readline()
        self.menu = Menu(name)
        settings.close()
        





        
main = Main()

