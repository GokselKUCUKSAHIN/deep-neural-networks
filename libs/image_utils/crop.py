from PIL import ImageFilter
from PIL import Image


def is_ARGB(image: Image) -> bool:
    return len( image.getpixel((0, 0))) is 4

def find_top_pixel(image: Image):
    for y in range(image.height):
        for x in range(image.width):
            r, g, b, a = image.getpixel((x, y))
            # print(f"x: {x:3}, y: {y:3} -> {(r, g, b, a)}")
            if a == 255:
                return y
    return -1


def find_bottom_pixel(image: Image):
    for y in range(image.height - 1, -1, -1):
        for x in range(image.width):
            r, g, b, a = image.getpixel((x, y))
            # print(f"x: {x:3}, y: {y:3} -> {(r, g, b, a)}")
            if a == 255:
                return y
    return -1


def find_left_pixel(image: Image):
    for x in range(image.width):
        for y in range(image.height):
            r, g, b, a = image.getpixel((x, y))
            # print(f"x: {x:3}, y: {y:3} -> {(r, g, b, a)}")
            if a == 255:
                return x
    return -1


def find_right_pixel(image: Image):
    for x in range(image.width - 1, -1, -1):
        for y in range(image.height):
            r, g, b, a = image.getpixel((x, y))
            # print(f"x: {x:3}, y: {y:3} -> {(r, g, b, a)}")
            if a == 255:
                return x
    return -1


def find_crop_edges(image: Image):
    left = find_left_pixel(image)
    top = find_top_pixel(image)
    right = find_right_pixel(image)
    bottom = find_bottom_pixel(image)
    return left, top, right, bottom


def crop_object_and_strech(image: Image) -> Image:
    if not is_ARGB(image):
        raise ValueError("Image format has to be ARGB!")
    og_size = image.size
    filtered_img = image.filter(ImageFilter.MedianFilter)
    crop_edge = find_crop_edges(filtered_img)
    return image.crop(crop_edge).resize(og_size)
