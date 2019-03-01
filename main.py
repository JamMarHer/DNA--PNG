import sys
from JsonProcessing import JsonProcessing
from ImageProcessing import ImageProcessing

COLORS_PATH ='colorValues.json'
REPORT_PATH = None



if __name__ == '__main__':
    jsonP = None

    fromCommand = False
    if REPORT_PATH is None:
        if (sys.argv[1:][0].split(".")[-1] != "txt"):
            # TODO eh it could technically in other format, good for now.
            print("Please make sure that the file is in txt format")
        else:
            fromCommand = True
            jsonP = JsonProcessing(sys.argv[1:][0])
    else:
        jsonP = JsonProcessing(REPORT_PATH)
    jsonP.initialize()
    colorsDic = jsonP.getJSONasDic(COLORS_PATH)
    if fromCommand:
        imageP = ImageProcessing(jsonP, colorsDic, sys.argv[2:])
    else:
        imageP = ImageProcessing(jsonP, colorsDic, sys.argv[1:])
    imageP.displayImage()
