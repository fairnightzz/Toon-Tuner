class Btn:
    def __init__(self,up,down,x,y):
        self.pressed=False
        self.rect=(x,y)
        self.up = up
        self.down = down

    def draw(self,screen):
        screen.blit([self.up,self.down][self.pressed],(self.rect[0],self.rect[1]))

