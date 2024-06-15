given the head of single linked list, rverse the linked list and return the reversed link list.
given the head of a single linked list and an integer k. find thekth node of the linked list from the last and delete the same

=
class Node:
    def __init__(self) -> None:
            self.value = value 
            self.next = None
class LinkedList:
    def __init__(self) -> None:
          self.head = None

    def inset(self,value):
        node = Node(value)
        if self.head =None:
            self.head = node 
            return
        temp = self.head 
        self.head = node
        node.next = temp
    def delete(self):
        self.head = self.head.next

    def display: 