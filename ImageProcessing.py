from PIL import Image
import numpy as np
from JsonProcessing import JsonProcessing
from random import randint
from AudioLogic import AudioLogic
import time
from JsonProcessing import JsonProcessing

class ImageProcessing(object):
    """docstring for ImageProcessing."""

    def __init__(self, jp, colors, genosToShow=None):
        super(ImageProcessing, self).__init__()
        self.jp = jp
        accert(jp, JsonProcessing())
        accert(jp.isinitialized() == True)
        self.genosToShow = genosToShow
        self.colors = colors
        self.al = AudioLogic()

    def displayImage(self):
        width = 700
        height = 700
        channels = 3

        JsonP = JsonProcessing(self.DNAJSON)
        #genodict, genoKeys = JsonP.getOrderedGenotypeKeyDict()
        #genoorderedList = JsonP.getOrderedGenotypeList(genodict, genoKeys)
        #JsonP.saveList("genotypeByPosition", genoorderedList)

        self.genoList = JsonP.loadList("genotypeByPosition.dna")
        # Set the RGB values
        print("Processing...")
        img = self.getImage(height, width, channels, self.genosToShow)
        img.show()
        print("Genotype {} save...".format("all"))
        print("Done.")
        # Display the image

    def getImage(self, height, width, channels, geno=None):
        position = 0
        img = np.zeros((height, width, channels), dtype=np.uint8)
        for y in range(img.shape[0]):
            for x in range(img.shape[1]):
                position += 1
                r, g, b = self.getColors(x, y, position, geno)
                img[y][x][0] = r
                img[y][x][1] = g
                img[y][x][2] = b
        img = Image.fromarray(img)
        return img

    def getColors(self, x, y, position, targetGeno=None):
        geno = self.genoList[position]
        if(targetGeno):
            if (geno in targetGeno):
                self.al.play()
                return self.colors[geno]["r"], self.colors[geno]["g"], self.colors[geno]["b"]
            time.sleep(.001)
            return 0, 0 ,0
        return self.colors[geno]["r"], self.colors[geno]["g"], self.colors[geno]["b"]

    def playWithColors(self, colors):
        toReturn = dict()
        r, g, b = 135, 48, 100

        for geno in colors:
            toReturn[geno] = dict()
            toReturn[geno]["r"] = r
            toReturn[geno]["g"] = g
            toReturn[geno]["b"] = b
            r += 10
            g += 10
            b += 10
        return toReturn
