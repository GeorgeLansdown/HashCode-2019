import math

def value(L,x):
  low = []
  med = []
  high = []
  if L%3==0:
    print(L//3)
    print(2*L//3)
    for i in range(1,L//3+1):
      low.append(i)
    for i in range((L//3)+1,((2*L)//3+1)):
      med.append(i)
    for i in range(((2*L)//3)+1,L+1):
      high.append(i)
  else:
    for i in range(1,math.floor(L//3+1)):
      low.append(i)
    for i in range(math.ceil(L//3)+1,math.floor((2*L)//3+1)):
      med.append(i)
    for i in range(math.ceil((2*L)//3)+1,L+1):
      high.append(i)
  if x == "low":
      return low
  elif x == "med":
      return med
  elif x == "high":
      return high
