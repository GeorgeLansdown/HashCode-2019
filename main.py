#hashcode 2019 George Lansdown Liana Ahmed Michael Aylesbury
from pic import *


class main:

    collectionSize = 0
    inputPics = []
    outputPics = []

    dir = ""
    horizontal = 0
    vertical = 0

    def __init__(self, dir):
        self.collectionSize = 0
        self.inputPics = []
        self.dir = dir
        self.horizontal = 0
        self.vertical = 0

        with open(dir, "r") as all:
            file = all.read().split("\n")
            self.collectionSize = int(file[0])
            id = 0

            for f in file[1:-1]:
                n = f.split(" ")

                p = pic(n[0], str(id))
                if n[0] == "H":
                    self.horizontal += 1
                else:
                    self.vertical += 1

                id += 1

                for g in n[2:]:
                    p.addTag(g)
                self.inputPics.append(p)

    def getCollectionSize(self):
        return self.collectionSize

    def getinputPics(self):
        return self.inputPics

    def getSimilar(self):
        for f in range(0, len(self.inputPics)):
            for g in range(f+1, len(self.inputPics)):
                print(self.inputPics[f].similarTags(self.inputPics[g]))

    def interestFactor(self, pic1, pic2):
        common = len(pic1.similarTags(pic2))
        firstButNotSecond = len(pic1.getTags())-common
        secondButNotFirst = len(pic2.getTags())-common

        return min(common, firstButNotSecond, secondButNotFirst)

    def overallInterestFactor(self):
        sum = 0
        if len(self.inputPics) == 0:
            return sum
        for f in range(0, len(self.inputPics)-1):
            sum += self.interestFactor(self.inputPics[f], self.inputPics[f+1])
        return sum

    def printAll(self):
        print(self.collectionSize)
        for f in self.inputPics:
            print(f)

    def output(self, inputPics):
        slidesNumber = int(self.horizontal+(self.vertical/2))

        with open("out"+self.dir, "w+") as file:
            file.write(str(slidesNumber)+"\n")
            otherPic = pic("H", "-1")
            for f in inputPics:
                if f.getOrientation() == "H":
                    file.write(str(f.getID())+"\n")
                else:
                    if otherPic.getOrientation() == "H":
                        otherPic = f
                    else:
                        otherPic = f.joinWith(otherPic)
                        file.write(str(otherPic.getID())+"\n")
                        otherPic = pic("H", "-1")


#Splitting into horizontal and vertical
def splitHV(inputPics):0
  horiz = []
  vert = []
  for f in inputPics:
    if f.getOrientation() == 'H':
      horiz.append(f)
    else:
      vert.append(f)

    return (horiz, vert)

#Assume slides are given as an array,
#This takes the slides and checks no two adjacent slides have no similarity
def simCheck(slides):
  for s in range(0,len(slides)):
    if slides[s].similarTags(slides[s+1])==0:
      raise Exception("No similarity")

<<<<<<< HEAD

if __name__ == "__main__":
  IOdir = input("File?")
  m = main(IOdir+".txt")
  m.output(m.getinputPics())
=======
def commonTags(photos):

    sortedList = []
    currentTuple = []


    for i in photos:
        
        wordTuples = []
        
        for j in range(1, len(photos)):
            
            count = i.getSimilar(photos[j])
                
            if count == 0:
                next
            else:
                currentTuple = (j, count)
                wordTuples.append(currentTuple)
        
        sortedList.append(wordTuples)
    
    return sortedList
>>>>>>> 68e397aadf0ca0c3e14c710083e40703fc4650af
