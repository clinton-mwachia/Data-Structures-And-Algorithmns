class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        nodes = []
        while temp is not None:
            nodes.append(temp.data)
            temp = temp.next
        nodes.append('None')
        print(" --> ".join(nodes))


if __name__ == '__main__':

    llist = LinkedList()
    llist.head = Node('1')
    second = Node('2')
    third = Node('3')
    four = Node('10')
    fifth = Node('900')

    # linking the head node to the second node
    llist.head.next = second
    # linking the second node to the third node
    second.next = third
    third.next = four
    four.next = fifth
    llist.printList()
