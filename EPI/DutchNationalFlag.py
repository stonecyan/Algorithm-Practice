def dutchFlagPartition(list,pivot):
  smaller = 0
  equal = 0
  larger = len(list)-1

  while equal<larger:
    if list[equal]<pivot:
      list[smaller], list[equal] = list[equal], list[smaller]
      smaller+=1
      equal+=1
    elif list[equal]==pivot:
      equal+=1
    elif list[equal]>pivot:
      list[larger], list[equal] = list[equal], list[larger]
      larger-=1
      equal+=1
  return list


x = [0,1,2,0,2,1,1]
pivot = 1
y=dutchFlagPartition(x,pivot)
print(y)
