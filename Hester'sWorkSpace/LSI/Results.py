class Results:
    numOfResults = 0
    matchingLines = {} #{similarity:(docName, [hit lines]) }
    hitDocs = {}  # {lengthHits:(docName,[hit lines])}
    fullHitLines = {}  # {fullHitNum:(docName,[hit lines])}

    def __init__(self, numOfResults=0, matchingLines={},hitDocs={},fullHitLines={}):
        self.numOfResults = numOfResults
        self.matchingLines = matchingLines
        self.hitDocs=hitDocs
        self.fullHitLines=fullHitLines

    def getNumOfResults(self):
        return self.numOfResults

    def setNumOfResult(self, num):
        self.numOfResults = num

    def getMatchingLines(self):
        return self.matchingLines

    def setMatchingLines(self, matchingLines):
        self.matchingLines = matchingLines

    def getHitDocs(self):
        return self.hitDocs

    def setHitDocs(self, hitDocs):
        self.hitDocs=hitDocs

    def getFullHitLines(self):
        return self.fullHitLines

    def setFullHitLines(self,fullHitLines):
        self.fullHitLines=fullHitLines

    def to_string(self):
        print('num of results:')
        print(self.numOfResults)
        print('full hit docs:')
        print(self.fullHitLines)
        print('hit docs')
        print(self.hitDocs)
        # print('matching docs:')
        # print(self.matchingLines)

