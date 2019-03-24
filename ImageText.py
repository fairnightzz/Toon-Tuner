import io
from TextCell import *
from pygame import *
from TextBox import *
# Imports the Google Cloud client library
from google.cloud import vision


class ImageText():
    client = vision.ImageAnnotatorClient()
    def __init__(self,file_name,image,x,y):
        self.image=image
        self.x=x
        self.y=y
        self.text_boxes=[]
        boxes=ImageText.getBoxes(image.copy())

        """Detects text in the file."""

        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)

        response = ImageText.client.text_detection(image=image)
        texts = response.text_annotations
        self.getTextBoxes(boxes,[textcell(i) for i in texts[1:]])
        print(self.text_boxes)
    @staticmethod
    def getBoxes(surface):
        
        array = PixelArray(surface)

        textboxes = []
        dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        for y in range(array.shape[1]):
            for x in range(array.shape[0]):
                if array[x, y] == surface.map_rgb((255, 255, 255)):
                    queue = [(x, y)]
                    points = [(x, y)]
                    while queue:
                        cur = queue.pop()
                        for d in dirs:
                            if 0 <= cur[0] + d[0] < array.shape[0] and 0 <= cur[1] + d[1] < array.shape[1]:
                                nex = array[cur[0] + d[0], cur[1] + d[1]]
                                if surface.map_rgb((240, 240, 240)) <= nex:
                                    points.append((cur[0] + d[0], cur[1] + d[1]))
                                    queue.append((cur[0] + d[0], cur[1] + d[1]))
                                    array[cur[0], cur[1]] = (0, 0, 0)

                    leftX = min(points, key=lambda x: x[0])[0]
                    rightX = max(points, key=lambda x: x[0])[0]
                    topY = min(points, key=lambda y: y[1])[1]
                    bottomY = max(points, key=lambda y: y[1])[1]
                    if len(points) >= 150:
                        textboxes.append(Rect(leftX, topY, rightX - leftX, bottomY - topY))

        return textboxes
    def getTextBoxes(self,boxes,text):

        for box in boxes:
            if box.width>self.image.get_width()-self.image.get_width()/10:
                continue
            b=TextBox(box,text)
            if not b.isEmpty():
                self.text_boxes.append(b)












# Instantiates a client


# The name of the image file to annotate


# Loads the image into memory
