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


def cyclicityTest(head):

    slow = fast = head
    while fast and fast.nextNode and fast.nextNode.nextNode:
        slow = slow.nextNode
        fast = fast.nextNode.nextNode
        if slow == fast:
            return slow.value
    return False


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
node5.nextNode = node1
l1.headval = node1

x = cyclicityTest(node1)
print(x)
