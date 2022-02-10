import moiveToImages
import ASCII
import ASCIIBackground
import combiningBodyAndBackground
import create_single_image
import imageToGIF
import movieLib
import colourLib
import fontLib
import charLib
import clearFolder

clearFolder.main(path="ASCII_frames")
clearFolder.main(path="bodyFrames")

count = 0
frameExist = True
movieUsed = movieLib.main()
colourListUsed = colourLib.main()
fontTypeUsed = fontLib.main()
charUsed = charLib.main()

print(movieUsed)
print(colourListUsed)
print(fontTypeUsed)
print(charUsed)

moiveToImages.main(moviePath=movieUsed)
while frameExist:
    try:
        ASCII.main(asciiCharts=charUsed, path='bodyFrames\\frame%d.png' %count)
        ASCIIBackground.main(path='backgroundFrames\\frame%d.png' %count)
        combiningBodyAndBackground.main(asciiCharts=charUsed, bodyPath="ascii_image.txt", backgroundPath="ascii_image_background.txt")
        create_single_image.main(asciiCharts=charUsed, fontType=fontTypeUsed, colourList= colourListUsed, save_name='ASCII_frames\\ASCII_frame%d.png' %count)
        count += 1
    except:
        frameExist = False

imageToGIF.main()
