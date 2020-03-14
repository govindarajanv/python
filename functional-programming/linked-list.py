"""
Node Object for setting the data and pointer to NULL
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

"""
Linkedlist with its head pointing to None 
"""
class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self): 
        temp = self.head 
        while (temp): 
            print temp.data, 
            temp = temp.next

if __name__ == '__main__':
    
    # Create a linked list object
    llist = LinkedList()

    # Create the first node
    node1 = Node(1)

    # Linked List Head to point to first node
    llist.head = node1

    # Create second and third nodes
    node2 = Node(2)
    node3 = Node(3)

    # Linked Nodes

    llist.head.next = node2
    node2.next = node3

    #printing linked list
    llist.printList() 
    









