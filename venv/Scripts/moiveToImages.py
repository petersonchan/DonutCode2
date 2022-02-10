import cv2

def main(moviePath=""):
  vidcap = cv2.VideoCapture(moviePath)
  success,image = vidcap.read()
  count = 0
  while success:
    cv2.imwrite("bodyFrames\\frame%d.png" % count, image)     # save frame as JPEG file
    success,image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1

if __name__ == '__main__':
  main(moviePath="")