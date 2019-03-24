from google.cloud import translate
class textcell:

    def __init__(self,label):
        self.x,self.y=label.bounding_poly.vertices[0].x,label.bounding_poly.vertices[0].y

        self.width=label.bounding_poly.vertices[1].x-label.bounding_poly.vertices[0].x
        self.height=label.bounding_poly.vertices[2].y-label.bounding_poly.vertices[1].y
        self.text=label.description












