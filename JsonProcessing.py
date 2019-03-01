import pickle

class JsonProcessing(object):

    """ This class provides multiple functions for processing a DNA input that is
        already in JSON ordered format:
        Chormosome (int):
            RSID(str):
                Position(str)
                Genotype(str)
    """

    def __init__(self, data):
        super(JsonProcessing, self).__init__()
        assert(data, dict())
        self.data = data


    def getOrderedPositionList(self):
        listPosition = list()
        newOrderedDict = dict()
        for key, value in self.data.items():
            for key2, value2 in value.items():
                newOrderedDict[value2["position"]] = value2["genotype"]
                listPosition.append(value2["position"])
        listPosition.sort()
        return listPosition

    def getOrderedGenotypeKeyDict(self):
        newOrderedDict = dict()
        keyList = list()
        for key, value in self.data.items():
            for key2, value2 in value.items():
                newOrderedDict[value2["position"]] = value2["genotype"]
                keyList.append(value2["position"])
        keyList.sort()
        return newOrderedDict, keyList

    def getOrderedGenotypeList(self, newOrderedDict, keyList):
        orderedList = self.getOrderedPositionList()
        orderderedGenotypeList = list()
        count = 0
        lengthOf = len(orderedList)
        for position in keyList:
            count  += 1
            orderderedGenotypeList.append(newOrderedDict[position])
            print ("[{}/{}]".format(count, lengthOf))
        return orderderedGenotypeList

    def saveList(self, name, toDump):
        with open("{}.dna".format(name), 'wb') as fp:
            pickle.dump(toDump, fp)

    def loadList(self, name):
        with open (name, 'rb') as fp:
            itemlist = pickle.load(fp)
        return itemlist
