from google.cloud import translate
import textwrap
def wrap(s,w):
    wrapper=textwrap.TextWrapper(width=w)
    return wrapper.wrap(text=s)
    
class TextBox():
    translate_client = translate.Client()
    target = "en"
    source = "ko"
    def __init__(self,box,text,fontN):
        contained=[]
        
        for cell in text:
            if box.x<cell.x and box.y<cell.y and box.x+box.width>cell.x+cell.width and box.y+box.height<cell.y+cell.height:
                contained.append(cell)
        self.text = list(TextBox.translate_client.translate(
            " ".join(c.text for c in contained),
            source_language=TextBox.source,
            target_language=TextBox.target).values())[0]
        
        if self.text:
            self.x=box.x
            self.y=box.y
            self.width=box.width
            self.height=box.height
            
            wrapped = wrap(self.text,self.width)
            textBox=fontN.render(wrapped,True,(255,255,255))
            screen.blit(textBox,(box.x,box.y))
            










    def isEmpty(self):
        return self.text==""

