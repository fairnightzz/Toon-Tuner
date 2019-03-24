import io
import os
from TextCell import *
from math import *
from pygame import *
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
class ImageText():
    client = vision.ImageAnnotatorClient()
    def __init__(self,file_name,image):
        self.text_boxes=[]
        """Detects text in the file."""

        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)

        response = ImageText.client.text_detection(image=image)
        texts = response.text_annotations
        self.text=textcell(texts[0])

    def getTextboxes(surface):
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
                        textboxes.append((leftX, topY, rightX - leftX, bottomY - topY))

        return textboxes











# Instantiates a client


# The name of the image file to annotate


# Loads the image into memory
