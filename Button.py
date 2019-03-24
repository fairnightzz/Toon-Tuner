class Button():
    def __init__(self,up,down,rect):
        self.pressed=False
        self.rect=rect

    def draw(self,screen):
        screen.blit((self.rect.x,self.rect.y),[self.up,self.down][self.pressed])

