import random

def randomSampling(x, list):
  for i in range(x):
    r=random.randint(i,len(list)-1)
    list[i], list[r] = list[r], list[i]
  return list[0:x]


a=[3,5,6,11]
y=randomSampling(3,a)
print(y)
