# How To Use
# In command Line:
# > python3 makeRound.py <imageName>

import sys
import numpy as np 
from PIL import Image, ImageDraw 

def main(argv):
    numberImages = len(argv)
    for i in range(1, numberImages):
        fullFilename = argv[i]
        filename = fullFilename.split(".")[0]

        print("Starting rounding " + filename)

        originalImg = Image.open("./" + argv[i]) 
        maskImg = Image.new('L', originalImg.size, 0)
        draw = ImageDraw.Draw(maskImg)
        draw.ellipse ((0,0,originalImg.size), fill='white')
        #maskImg.show()
        emptyImg = Image.new('RGBA', originalImg.size, (0,0,0,0))
        #emptyImg.show()
        resultImg = Image.composite(originalImg, emptyImg, maskImg)
        #resultImg.show()

        resultImg.save(filename + "_round" + ".png")

        print("Finished rounding " + filename)


if __name__ == "__main__":
    main(sys.argv)
