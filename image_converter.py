from PIL import Image, ImageOps
from io import BytesIO

class ImageConverter:
    def __init__(self, file):
        self.file = file

    def invert(self):
        image = Image.open(self.file)
        inverted_image = ImageOps.invert(image.convert("RGB"))

        buffer = BytesIO()
        inverted_image.save(buffer, format="png")
        image_bytes = buffer.getvalue()
        return image_bytes