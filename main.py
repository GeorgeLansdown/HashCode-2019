#hashcode 2019 George Lansdown Liana Ahmed Michael Aylesbury
from pic import *


class main:

    collectionSize = 0
    pics = []

    dir = ""
    horizontal = 0
    vertical = 0

    def __init__(self, dir):
        self.collectionSize = 0
        self.pics = []
        self.dir = dir
        self.horizontal = 0
        self.vertical = 0

        with open(dir, "r") as all:
            file = all.read().split("\n")
            self.collectionSize = int(file[0])
            id = 0

            for f in file[1:-1]:
                n = f.split(" ")

                p = pic(n[0], id)
                if n[0] == "H":
                    self.horizontal += 1
                else:
                    self.vertical += 1

                id += 1

                for g in n[2:]:
                    p.addTag(g)
                self.pics.append(p)

    def getCollectionSize(self):
        return self.collectionSize

    def getPics(self):
        return self.pics

    def getSimilar(self):
        for f in range(0, len(self.pics)):
            for g in range(f+1, len(self.pics)):
                print(self.pics[f].similarTags(self.pics[g]))

    def interestFactor(self, pic1, pic2):
        common = len(pic1.similarTags(pic2))
        firstButNotSecond = len(pic1.getTags())-common
        secondButNotFirst = len(pic2.getTags())-common

        return min(common, firstButNotSecond, secondButNotFirst)

    def overallInterestFactor(self):
        sum = 0
        if len(self.pics) == 0:
            return sum
        for f in range(0, len(self.pics)-1):
            sum += self.interestFactor(self.pics[f], self.pics[f+1])
        return sum

    def printAll(self):
        print(self.collectionSize)
        for f in self.pics:
            print(f)

    def output(self):
        with open("out"+self.dir, "w+") as file:
            file.write()


if __name__ == "__main__":
  IOdir = input("File?")
  main(IOdir+".txt")










#Splitting into horizontal and vertical
def splitHV(pics):
  horiz = []
  vert = []
  for f in pics:
    if f.getOrientation() == 'H':
      horiz.append(f)
    else:
      vert.append(f)

#Assume slides are given as an array,
#This takes the slides and checks no two adjacent slides have no similarity
def simCheck(slides):
  for s in range(0,len(slides)):
    if slides[s].similarTags(slides[s+1])==0:
      raise Exception("No similarity")
