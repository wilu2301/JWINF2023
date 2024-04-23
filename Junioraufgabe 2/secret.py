"""JWINF 2023 Runde 3 Aufgabe 2: St. Egano
Assets: https://bwinf.de/bundeswettbewerb/42/1"""

from PIL import Image
import pathlib


def read_image(path: str) -> Image.Image:
    """
    Reads an image from the given path and returns it as an Image object.
    :arg path: The path to the image in the filesystem.
    :returns: A PIL Image object.
    """
    return Image.open(path).convert("RGB")


def process_pixel(rgb: list, position: tuple, ctx: Image.Image) -> list:
    """
    Processes the given pixel and returns a list containing the ascii char
    and next pixel location
    :param ctx: The Image Object
    :param position:The Location of this pixel
    :param rgb: The given Pixel as RGB value
    :return:A list with the ascii char and net position
    """
    letter: str = chr(rgb[0])
    right: int = rgb[1]
    down: int = rgb[2]

    if down == 0 and right == 0:
        # Sends an end flag to the while loop
        return [letter, (-1, -1)]

    new_postion: tuple = calculate_new_postion(position, right, down, ctx)
    return [letter, new_postion]


def calculate_new_postion(current: tuple, right: int, down: int, ctx: Image.Image) -> tuple:
    """
    Calculates the new relative postion of a given pixel
    :param current:The current absolute postion
    :param right: The amount of pixels it should go to the right
    :param down: The amount of pixels it should go down
    :param ctx: The PIL Image object to check the dimensions

    :return: A tuple of the new absolute position.
    """
    current_list = list(current)

    current_list[0] = (right + current_list[0]) % ctx.width
    current_list[1] = (down + current_list[1]) % ctx.height

    return tuple(current_list)


def resolve_image(image_path: str) -> str:
    """
    Resolves the hidden message of a given image path
    :param image_path: The path, where the image is located
    :return: The encoded message as string
    """
    image = read_image(image_path)

    current_postion: tuple = (0, 0)
    secret_code: str = ""
    while True:
        rgb: list = image.getpixel(current_postion)
        result: list = process_pixel(rgb, current_postion, image)
        secret_code += (result[0])
        current_postion = result[1]

        # End Flag
        if current_postion == (-1, -1):
            break
    return secret_code


def main():
    """Main Interface for a basic CLI"""

    print("[Image solver] Please enter your image location file")
    file_input: str = input("->")
    if not file_input:
        print("No path entered, try again!")
        return

    file: pathlib.Path = pathlib.Path(file_input)
    if not file.is_file():
        print("No valid file, try again!")
        return

    if file.suffix not in {".jpg", ".jpeg", ".png", ".tiff"}:
        print("No valid file extension, try again")
        return

    print(resolve_image(str(file)))


if __name__ == "__main__":
    main()
