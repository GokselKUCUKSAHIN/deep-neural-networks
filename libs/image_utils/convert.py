from typing import Tuple
from PIL import Image


def fill_background(image: Image, bg_color: Tuple[int, int, int]) -> Image:
    background = Image.new('RGBA', image.size, bg_color)
    return Image.alpha_composite(background, image)