import pickle
import json
import sys

class JsonProcessing(object):

    """ This class provides multiple functions for processing a DNA input that is
        already in original format then it orders it in json:
        Chormosome (int):
            RSID(str):
                Position(str)
                Genotype(str)
    """

    def __init__(self, path):
        super(JsonProcessing, self).__init__()
        assert(data, str)
        self.data = self.saveDNAinputAsOrderedJSON(path)

    def saveDNAinputAsOrderedJSON(path):
        dataForJson = {'X':dict(), 'Y':dict(), 'MT':dict()}
        for x in range(1, 23):
            dataForJson[str(x)] = dict()
        with open (path) as f:
            data = f.readlines()
        for line in data:
            tline = line.replace('\n', '').split('\t')
            dataForJson[tline[1]][tline[0]] = {'position' : tline[2], 'genotype' : tline[3]}

        with open("{}.json".format(path.split('.')[0]), "w") as fp:
            json.dump(dataForJson, fp,sort_keys=True, indent=4, separators=(',', ': '))
        return dataForJson

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
