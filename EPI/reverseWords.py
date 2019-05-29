def reverseWords(s):
  def reverse(s,start,end):
    while start<end:
      s[start], s[end] = s[end], s[start]
      start+=1
      end-=1
  
  reverse(s,0,len(s)-1)

  start=0
  while True:
    end=start
    while end<len(s) and s[end] != " ":
      end +=1
    if end == len(s):
      break
    reverse(s,start,end-1)
    start=end+1
  reverse(s,start,len(s)-1)

  return s

x=reverseWords(["b","a","l","l"," ","i","s"," ","l","i","f","e"])
print(x)
