from rembg import remove
from PIL import Image


def remove_background(image: Image.Image) -> Image.Image:
    """
    Remove background from an image using rembg.
    """
    output = remove(image)
    return output