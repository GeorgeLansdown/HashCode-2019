class pic:
    orientation = ""
    ID = ""
    tags = []
    numberOfTags = 0


    def __init__(self, orientation, ID):
        self.setID(ID)
        self.setOrientation(orientation)

    def getID(self):
        return self.ID

    def setID(self, v):
        self.ID = v

    def setOrientation(self, v):
        if (v=="H" or v == "V"):
            self.orientation = v
        else:
            print("invalid orientation: "+v)

    def getOrientation(self):
        return self.orientation

    def getTags(self):
        return self.tags

    def addTag(self, t):
        self.tags.append(t)
        self.numberOfTags += 1

    def getNumberOfTags(self):
        return self.numberOfTags

    def __str__(self):
        o = orientation+" "+self.numberOfTags
        for f in self.tags:
            o+=" "+f
