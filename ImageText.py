import io
import os
from TextCell import *

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
class ImageText():
    client = vision.ImageAnnotatorClient()
    def __init__(self,file_name):
        """Detects text in the file."""

        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)

        response = ImageText.client.text_detection(image=image)
        texts = response.text_annotations



        self.cells=[textcell(text) for text in texts]



# Instantiates a client


# The name of the image file to annotate


# Loads the image into memory
