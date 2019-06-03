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


def evenOddMerge(node):
    if node is None:
        return node

    evenDummyHead = Node(0)
    oddDummyHead = Node(0)

    even = evenDummyHead
    odd = oddDummyHead

    while node:
        odd.next = node
        node = node.next
        odd = odd.next
        if node:
            even.next = node
            node = node.next
            even = even.next
    odd.next = None
    even.next = oddDummyHead.next
    return evenDummyHead.next


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

y = LinkedList()
y.headval = evenOddMerge(n1)
y.printlist()
