from PIL import Image, ImageFont, ImageDraw
import ASCII as ascii


def main(asciiCharts=[], fontType = "", colourList = [], save_name = 'ASCII_frames\\ASCII_frame0.png'):
    #f = open("ascii_image.txt", "r")
    f = open("ascii_image_combined.txt", "r")
    to_text = f.read()

    color_Bg = colourList[5]
    color_0 = colourList[0]
    color_1 = colourList[1]
    color_2 = colourList[2]
    color_3 = colourList[3]
    color_4 = colourList[4]

    img = Image.new('RGBA', (1500,1450), color_Bg)
    str = to_text
    font = ImageFont.truetype(fontType, 30) #60 if 15 width / 25 height for 1 character

    w, h = font.getsize(str)

    draw = ImageDraw.Draw(img)
#   draw.text((0, 0), str, font=font, fill='white')

# size = (30 * (i % 51), 58 * row) if textSize = 60
# size = (15 * (i % 101), 29 * row) if textSize = 30
    row = 0
    for i in range(len(str)):
        if str[i] != "\n":
            if str[i] == asciiCharts[0]:
                draw.text((15 * (i % 101), 29 * row), str[i], font=font, fill=color_0)
            elif str[i] == asciiCharts[1]:
                draw.text((15 * (i % 101), 29 * row), str[i], font=font, fill=color_1)
            elif str[i] == asciiCharts[2]:
                draw.text((15 * (i % 101), 29 * row), str[i], font=font, fill=color_1)
            elif str[i] == asciiCharts[3]:
                draw.text((15 * (i % 101), 29 * row), str[i], font=font, fill=color_2)
            elif str[i] == asciiCharts[4]:
                draw.text((15 * (i % 101), 29 * row), str[i], font=font, fill=color_2)
            elif str[i] == asciiCharts[5]:
                draw.text((15 * (i % 101), 29 * row), str[i], font=font, fill=color_2)
            elif str[i] == asciiCharts[6]:
                draw.text((15 * (i % 101), 29 * row), str[i], font=font, fill=color_3)
            elif str[i] == asciiCharts[7]:
                draw.text((15 * (i % 101), 29 * row), str[i], font=font, fill=color_3)
            elif str[i] == asciiCharts[8]:
                draw.text((15 * (i % 101), 29 * row), str[i], font=font, fill=color_3)
            elif str[i] == asciiCharts[9]:
                draw.text((15 * (i % 101), 29 * row), str[i], font=font, fill=color_4)
            elif str[i] == asciiCharts[10]:
                draw.text((15 * (i % 101), 29 * row), str[i], font=font, fill=color_4)
            else:
                draw.text((15 * (i % 101), 29 * row), str[i], font=font, fill='white')
        elif str[i] == "\n":
            row += 1

    #img.show()
    img.save(save_name)
    #print(w,h)

if __name__ == '__main__':
    main()