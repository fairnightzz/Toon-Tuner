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
        self.username = username
        if username == "Guest":
            print("Change username")
            
        else:
            print("Welcome",username)
        running=True
        loaded = False
        y = 0
        manga = image.load("Graphics/LightImport.png")
        self.dialog = ""
        current = "Main"
        mainl = ["New File","Open File","Settings"]
        mainpic = [Btn(image.load("Graphics/LightNew.png"),image.load("Graphics/LightNew#.png"),200,100)\
                   ,Btn(image.load("Graphics/LightOpen.png"),image.load("Graphics/LightOpen#.png"),\
                           200,300),Btn(image.load("Graphics/LightSettings.png"),image.load("Graphics/LightSettings#.png"),200,500)]
        pos = [[200,100],[200,300],[200,500]]

        editl = ["Import","Main","Save"]
        editpic = [Btn(image.load("Graphics/LightImport.png"),image.load("Graphics/LightImport#.png"),200,100)\
                   ,Btn(image.load("Graphics/LightMenu.png"),image.load("Graphics/LightMenu#.png"),\
                           200,300),Btn(image.load("Graphics/LightSave.png"),image.load("Graphics/LightSave#.png"),200,500)]
        
        #178,100
        
        mx,my = mouse.get_pos()
        while running:
            mx,my = mouse.get_pos()
            for evt in event.get():
                if evt.type == QUIT:
                    running = False
            #draw.rect(screen,(255,0,0),(100,100,400,400))
                if evt.type == MOUSEBUTTONDOWN:
                    if evt.button == 1:
                        if current == "Main":
                            for n in range(len(mainpic)):
                                if Rect(mainpic[n].rect[0],mainpic[n].rect[1],178,100).collidepoint(mx,my):
                                    #current = mainl[n]
                                    print(mainl[n])
                                    mainpic[n].pressed = True
                                    #dialog = self.newFile("Enter File Name")

                        elif current == "Edit":
                            for n in range(len(editpic)):
                                if Rect(editpic[n].rect[0],editpic[n].rect[1],178,100).collidepoint(mx,my):
                                    editpic[n].pressed = True

                    if evt.button == 4 and loaded:#scrolling up
                        x-=5
                    if evt.button == 5 and loaded: #scrolling down
                        x+=5
                    

                                
                if evt.type == MOUSEBUTTONUP:
                    if evt.button == 1:
                        if current == "Main":
                            for n in range(len(mainpic)):
                                mainpic[n].pressed = False
                            for n in range(len(mainpic)):
                                if Rect(mainpic[n].rect[0],mainpic[n].rect[1],178,100).collidepoint(mx,my):
                                    current = mainl[n]
                                    if current == mainl[0]:#New file
                                        self.dialog = self.newFile("Enter File Name")
                                        current = "Edit"
                                    elif current == mainl[1]:#Open file
                                        #dialog = self.
                                        print("in progresss")
                                        current = "Edit"
                                    elif current == main1[2]: #settings
                                        print("settings")

                        elif current == "Edit":
                            for n in range(len(editpic)):
                                editpic[n].pressed = False

                            for n in range(len(editpic)):
                                if Rect(editpic[n].rect[0],editpic[n].rect[1],178,100).collidepoint(mx,my):
                                    if n == 0:
                                        print("execute upload pic")
                                        link = self.importPic("Import picture link")
                                        print(self.dialog)
                                        download.download(download.get_imgs(link),"User Files/%s/"%(self.dialog))
                                        


                                        #Execute translation
                                        

                                        loaded = True                                    
                                    elif n == 2:
                                        if Rect(editpic[n].rect[0],editpic[n].rect[1],178,100).collidepoint(mx,my):
                                            save = open("Settings.txt","r+")
                                            save.close()

                                    elif n == 1:
                                        print("Leave")
                                        current = "Main"

                            
                                
                                
                        

                                    

                                    
            screen.fill((0,0,0))
            if current == "Main":
                for i in range(len(mainpic)):
                    mainpic[i].draw(screen)
            elif current == "Edit":
                for i in range(len(editpic)):
                    editpic[i].draw(screen)

                if loaded:
                    screen.blit(manga,(400,y))
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

    def importPic(self,message):
        test = takeInput(message)
        test.mainloop()
        link = test.returnmessage()
        return link


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

