from google.cloud import translate
import textwrap
def wrap(s,w):
    wrapper=textwrap.TextWrapper(width=w)
    return wrapper.wrap(text=s)
    
class TextBox():
    translate_client = translate.Client()
    target = "en"
    def __init__(self,box,text,fontN,screen):
        contained=[]
        self.fontN=fontN
        self.screen=screen
        for cell in text:
            if box.x<cell.x and box.y<cell.y and box.x+box.width>cell.x+cell.width and box.y+box.height<cell.y+cell.height:
                contained.append(cell)
        self.text = list(TextBox.translate_client.translate(
            " ".join(c.text for c in contained),
            target_language=TextBox.target).values())[0]
        
        if self.text:
            leftX=min(contained,key=lambda k: k.x)
            topY=min(contained,key=lambda k: k.y)
            rightX=max(contained,key=lambda k:k.x)
            bottomY=max(contained,key=lambda k:k.y)
            
            self.x=box.x
            self.y=box.y
            self.width=box.width
            self.height=box.height
            print(self.text)
            try:
                self.wrapped = wrap(self.text,self.width/8)
            except:
                self.wrapped = wrap(self.text,self.width)
            
            








    def drawN(self,img):
        for i in range(len(self.wrapped)):
                textBox=self.fontN.render(self.wrapped[i],True,(0,0,0))
                self.screen.blit(textBox,(self.x,self.y+i*20+img.y))
        

    def isEmpty(self):
        return self.text==""

