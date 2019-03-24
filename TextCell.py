from google.cloud import translate
class textcell:
    translate_client = translate.Client()
    target="en"
    source="ko"
    def __init__(self,label):
        self.x,self.y=label.bounding_poly.vertices[0].x,label.bounding_poly.vertices[0].y
        self.width=label.bounding_poly.vertices[1].x-label.bounding_poly.vertices[0].x
        self.height=label.bounding_poly.vertices[2].y-label.bounding_poly.vertices[1].y
        self.text=label.description
        self.translated=list(textcell.translate_client.translate(
            label.description,
            source_language=textcell.source,
            target_language=textcell.target).values())[0]










