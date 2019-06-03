def evaluateRPN(expression):
  intermediate = []
  operations = {"+": lambda x,y: x+y, "-": lambda x,y: x-y, "*": lambda x, y:x*y, "/": lambda x,y: x//y}

  for i in expression.split(','):
    if i in operations:
      intermediate.append(operations[i](intermediate.pop(),intermediate.pop()))
    else:
      intermediate.append(int(i))
  return intermediate[-1]

x=evaluateRPN("2,7,/")
print(x)
