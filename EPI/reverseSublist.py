class Node:    
  def __init__(self, value, nextNode=None):        
    self.value = value        
    self.nextNode = nextNode
class LinkedList:
    def __init__(self):
        self.headval = None
    def printlist(self):
        printval = self.headval
        while printval is not None:
            print (printval.value)
            printval = printval.nextNode
        

def reverseSublist(node, start, end):
  dummyHead = sublistStart = Node("dummy",node)
  for i in range(1, start):
    sublistStart = sublistStart.nextNode
  iterate = sublistStart.nextNode
  for i in range(end-start):
    temp = iterate.nextNode
    iterate.nextNode, temp.nextNode, sublistStart.nextNode = temp.nextNode, sublistStart.nextNode, temp
  return dummyHead.nextNode
  

l1 = LinkedList()
node1 = Node(11)
node2 = Node(3)
node3 = Node(5)
node4 = Node(7)
node5 = Node(2)
node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4
node4.nextNode = node5
l1.headval = node1

x=reverseSublist(node1, 2, 4)
l1.printlist()
