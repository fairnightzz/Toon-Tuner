class Button:
    def __init__(self,up,down,x,y):
        self.pressed=False
        self.rect=(x,y)

    def draw(self,screen):
        screen.blit((self.rect.x,self.rect.y),[self.up,self.down][self.pressed])

