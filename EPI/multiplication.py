def multiply(a, b):
  if (a[0]<0)^(b[0]<0):
    sign=-1
  else:
    sign=1
  a[0] = abs(a[0])
  b[0] = abs(b[0])
  
  sum = 0
  imultiplier = 0
  jmultiplier = 0
  for i in reversed(range(len(a))):
    for j in reversed(range(len(b))):
      sum+=a[j]*b[i]*10**jmultiplier*10**imultiplier
      jmultiplier+=1
      print(sum)
    jmultiplier=0
    imultiplier+=1
  sum=sum*sign
  return sum



a = [1,2,3]
b = [3,4,5]
x=multiply(a,b)
print(x)
