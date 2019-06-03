def evaluateRPN(expression):
  intermediate = []
  operations = {"+": lambda x,y: x+y, "-": lambda x,y: x-y, "*": lambda x, y:x*y, "/": lambda x,y: x//y}

  for character in expression.split(','):
    if character in operations:
      intermediate.append(operations[i](intermediate.pop(),intermediate.pop())
        intermediate.append(int(i))
  return intermediate[-1]

x=evaluateRPN("1234")
print(x)
