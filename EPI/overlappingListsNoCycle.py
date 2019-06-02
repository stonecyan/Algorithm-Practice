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


def overlappingListsNoCycle(l1, l2):
    def listLength(n):
        length = 0
        while n:
            length += 1
            n = n.nextNode
        return length
    longer = l2
    shorter = l1
    l1Length = listLength(l1)
    l2Length = listLength(l2)

    if l1Length > l2Length:
        longer = l1
        shorter = l2
    for i in range(abs(l1Length - l2Length)):
        longer = longer.nextNode
    while longer and shorter and longer is not shorter:
        longer = longer.nextNode
        shorter = shorter.nextNode
    return shorter


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

l2 = LinkedList()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.nextNode = n2
n2.nextNode = n3
l2.headval = n1

x = overlappingListsNoCycle(node1, n1)
print(x)
