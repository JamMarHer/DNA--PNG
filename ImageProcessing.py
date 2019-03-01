from PIL import Image
import numpy as np
from JsonProcessing import JsonProcessing
from random import randint
import time
from JsonProcessing import JsonProcessing

class ImageProcessing(object):
    """docstring for ImageProcessing."""

    def __init__(self, jp, colors, genosToShow=None):
        super(ImageProcessing, self).__init__()
        self.jp = jp
        assert jp, JsonProcessing()
        assert (jp.isInitialized() == True)
        self.genosToShow = genosToShow
        self.colors = colors

    def displayImage(self):
        width = 700
        height = 700
        channels = 3

        genodict, genoKeys = self.jp.getOrderedGenotypeKeyDict()
        self.genoList = self.jp.getOrderedGenotypeList(genodict, genoKeys)

        # Set the RGB values
        print("Processing...")
        img = self.getImage(height, width, channels, self.genosToShow)
        img.show()
        img.save('test.png')
        print("Genotype {} save...".format("all"))
        print("Done.")

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
                return self.colors[geno]["r"], self.colors[geno]["g"], self.colors[geno]["b"]
            return 0, 0 ,0
        return self.colors[geno]["r"], self.colors[geno]["g"], self.colors[geno]["b"]
