from PIL import Image, ImageOps
from io import BytesIO

class ImageConverter:
    def __init__(self, file):
        self._image = Image.open(file)
        # PIL package has an issue
        # when we run an image operation ( like .rotate )
        # then we lose a format property
        self._format = self._image.format

    def invert(self):
        self._image = ImageOps.invert(self._image.convert("RGB"))

    def rotate(self, angle):
        self._image = self._image.rotate(angle=angle)

    def mirror(self):
        self._image = ImageOps.mirror(self._image)

    def grayscale(self):
        self._image = ImageOps.grayscale(self._image)

    def get_image_bytes(self):
        buffer = BytesIO()
        self._image.save(buffer, format=self._format)
        return buffer.getvalue()