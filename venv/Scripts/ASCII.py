from PIL import Image

# ascii characters used to build the output text
#ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
#ASCII_CHARS = ["^","E", "E", "E", "L", "O", "W", "O", "E", "R", "!"]
#ASCII_CHARS = ["#", "O", "P", "E", "N", "S", "E", "A", "I", "O", "."]


# resize image according to a new width
# new_width=50 if textSize=60
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio /2)
    resized_image = image.resize((new_width, new_height))
    return (resized_image)


# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return (grayscale_image)


# convert pixels to a string of ascii characters
def pixels_to_ascii(image, asciiCharts=[]):
    pixels = image.getdata()
    characters = "".join([asciiCharts[pixel // 25] for pixel in pixels])
    return (characters)


def main(asciiCharts=[], new_width=100, path = 'bodyFrames\\frame0.png'):
    # attempt to open image from user-input
#    path = 'frames\\frame77.jpg'

    try:
        image = Image.open(path)
    except:
        print(path, " is not a valid pathname to an image.")

    # convert image to ascii
    new_image_data = pixels_to_ascii(grayify(resize_image(image)), asciiCharts=asciiCharts)

    # format
    pixel_count = len(new_image_data)
    ascii_image = "\n".join([new_image_data[index:(index + new_width)] for index in range(0, pixel_count, new_width)])

    #print result
    #print(ascii_image)

    # save result to "ascii_image.txt"
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)


# run program
if __name__ == '__main__':
    main(new_width=50, path='bodyFrames\\frame0.png', asciiCharts=ASCII_CHARS)