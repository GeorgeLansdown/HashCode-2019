#hashcode 2019 George Lansdown Liana Ahmed Michael Aylesbury
from pic import *


class main:

    collectionSize = 0
    pics = []

    def __init__(self, dir):
        self.collectionSize = 0
        self.pics = []

        with open(dir, "r") as all:
            file = all.read().split("\n")
            self.collectionSize = int(file[0])
            id = 0

            for f in file[1:-1]:
                n = f.split(" ")

                p = pic(n[0], id)
                id += 1

                for g in n[2:]:
                    p.addTag(g)
                self.pics.append(p)

    def getCollectionSize(self):
        return self.collectionSize

    def getPics(self):
        return self.pics

    def printAll(self):
        print(self.collectionSize)
        for f in self.pics:
            print(f)


if __name__ == "__main__":
  IOdir = input("File?")
  m = main(IOdir+".txt")
