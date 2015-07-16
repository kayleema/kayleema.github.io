import os
import sys
from PIL import Image

def resize(folder, fileName, width):
    filePath = os.path.join(folder, fileName)
    im = Image.open(filePath)
    w, h  = im.size
    newIm = im.resize((int(width), int(h*float(width)/w+0.5)), Image.ANTIALIAS)
    # i am saving a copy, you can overrider orginal, or save to other folder
    folder = os.path.join(folder, "resize/")
    filePath = os.path.join(folder, fileName)
    print filePath+".jpeg"
    newIm.save(filePath+".jpeg")

def bulkResize(imageFolder, width):
    imgExts = ["jpg"]
    for path, dirs, files in os.walk(imageFolder):
        for fileName in files:
            ext = fileName[-3:].lower()
            if ext not in imgExts:
                continue
            print path
            print fileName
            resize(path, fileName, width)
            print "========"
            #resize(path, fileName, width)

if __name__ == "__main__":
    imageFolder=sys.argv[1] # first arg is path to image folder
    finalWidth=int(sys.argv[2])# 2nd is width
    bulkResize(imageFolder, finalWidth)
