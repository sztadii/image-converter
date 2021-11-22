from PIL import Image, ImageOps
from io import BytesIO

class ImageConverter:
    def __init__(self, _file):
        self._file = _file

    def invert(self):
        image = Image.open(self._file)
        inverted_image = ImageOps.invert(image.convert("RGB"))
        return self._transform_to_bytes(inverted_image)

    def rotate(self, angle):
        image = Image.open(self._file)
        rotated_image = image.rotate(angle=angle)
        return self._transform_to_bytes(rotated_image)

    def _transform_to_bytes(self, image):
        buffer = BytesIO()
        image.save(buffer, format="png")
        return buffer.getvalue()