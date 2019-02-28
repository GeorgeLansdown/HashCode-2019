#hashcode 2019 George Lansdown Liana Ahmed Michael Aylesbury
from pic import *

collectionSize = 0
pics = []

def main(dir):
  with open(dir, "r") as all:
      file = all.read()

      collectionSize = file[0]
      id = 0

      for f in file[1:]:
          print(f)

          n = f.split(" ")

          p = pic(n[0], id)
          id += 1

          for g in n[2:]:
              p.addTag(g)


def printAll():
    print("collectionSize = "+collectionSize)
    for f in pics:
        print(f)

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