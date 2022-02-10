from PIL import Image
import os.path

def main():
    images = []
    count = 0
    whileSwitch = True

    while whileSwitch:
        try:
            im = Image.open('ASCII_frames\\ASCII_frame%d.png' %count)
            images.append(im)
            count += 1
        except:
            whileSwitch = False

    countGifNum = 2
    while os.path.isfile('gif/pillow_imagedraw%d.gif' %countGifNum):
        countGifNum += 1

    images[0].save('gif/pillow_imagedraw%d.gif' %countGifNum,
               save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)

if __name__ == '__main__':
    main()