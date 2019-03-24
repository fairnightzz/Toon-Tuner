from pygame import*

class Menu:
    def __init__(self,username):
        if username == "":
            print("no username")
        else:
            print("Welcome",username)

class Main:
    def __init__(self):
        


menu = Menu("Nithin")
