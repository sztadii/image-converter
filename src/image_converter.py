from PIL import Image, ImageOps
from io import BytesIO

class ImageConverter:
    def __init__(self, file):
        self._image = Image.open(file)

    def invert(self):
        self._image = ImageOps.invert(self._image.convert("RGB"))

    def rotate(self, angle):
        self._image = self._image.rotate(angle=angle)

    def mirror(self):
        self._image = ImageOps.mirror(self._image)

    def get_image_bytes(self):
        buffer = BytesIO()
        self._image.save(buffer, format="png")
        return buffer.getvalue()