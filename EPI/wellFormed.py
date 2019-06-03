def wellFormed(s):
  left = []
  characters = {"{":"}", "(":")", "[":"]"}
  for char in s:
    if char in characters:
      left.append(char)
    elif not left or characters[left.pop()] != char:
      return False
  return not left

x="()[{}]"
print (wellFormed(x))
