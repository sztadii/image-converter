from PIL import Image, ImageOps
from io import BytesIO
from typing import IO

class ImageConverter:
    def __init__(self, file: IO):
        self._image = Image.open(file)
        # PIL package has an issue
        # when we run an image operation ( like .rotate )
        # then we lose a format property
        self._format = self._image.format

    def invert(self) -> None:
        self._image = ImageOps.invert(self._image.convert("RGB"))

    def rotate(self, angle: int) -> None:
        self._image = self._image.rotate(angle=angle)

    def mirror(self) -> None:
        self._image = ImageOps.mirror(self._image)

    def grayscale(self) -> None:
        self._image = ImageOps.grayscale(self._image)

    def get_image_bytes(self) -> bytes:
        buffer = BytesIO()
        self._image.save(buffer, format=self._format)
        return buffer.getvalue()