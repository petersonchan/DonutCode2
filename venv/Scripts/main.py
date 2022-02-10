import ASCII
import create_single_image
import imageToGIF

count = 0
whileSwitch = True

while whileSwitch:
    try:
        ASCII.main(path='bodyFrames\\frame%d.png' %count)
        create_single_image.main(save_name = 'ASCII_frames\\ASCII_frame%d.png' %count)
        count += 1
    except:
        whileSwitch = False

imageToGIF.main()