from google.cloud import translate
class TextBox():
    translate_client = translate.Client()
    target = "en"
    source = "ko"
    def __init__(self,box,text):
        contained=[]
        for cell in text:
            if box.x<cell.x and box.y<cell.y and box.x+box.width>cell.x+cell.width and box.y+box.height<cell.y+cell.height:
                contained.append(cell)
        self.text = list(TextBox.translate_client.translate(
            " ".join(c.text for c in contained),
            source_language=TextBox.source,
            target_language=TextBox.target).values())[0]
        if self.text:
            leftX=min(contained,key=lambda x:x.x).x
            rightX=min(contained,key=lambda x:x.x).x
            topY = min(contained, key=lambda y: y.y).y
            bottomY = max(contained, key=lambda y: y.y).y
            self.x=leftX
            self.y=topY
            self.width=rightX - leftX
            self.height=bottomY - topY










    def isEmpty(self):
        return self.text==""

