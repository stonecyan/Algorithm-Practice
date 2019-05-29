def replaceAndRemove(size,string):
  countA = 0
  currentIndex= 0
  for i in range(len(string)):
    if string[i] != "b":
      string[currentIndex]=string[i]
      currentIndex+=1
    if string[i] == "a":
      countA+=1
  print(string)
  trueLength = len(string)-1
  currentIndex=size
  writeIndex=trueLength
  while currentIndex>=0:
    if string[currentIndex]=="a":
      string[writeIndex] = "d"
      string[writeIndex-1] = "d"
      writeIndex -= 2
    else:
      string[writeIndex]=string[currentIndex]
      writeIndex -= 1
    currentIndex -= 1

  return string

x=replaceAndRemove(4,["a","c", "d", "b", "b", "c", "a"])
print(x)
