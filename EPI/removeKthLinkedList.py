class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.headval = None

    def printlist(self):
        printval = self.headval
        while printval is not None:
            print(printval.value)
            printval = printval.next


def removeKthElement(l1, k):
    dummyHead = Node(0, l1)
    first = dummyHead.next
    for i in range(k):
        first = first.next
    second = dummyHead
    while first:
        second = second.next
        first = first.next
    second.next = second.next.next
    return dummyHead.next


l = LinkedList()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
l.headval = node1

removeKthElement(node1, 3)
l.printlist()
