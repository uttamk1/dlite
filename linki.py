class Node:
    def __init__(self,value) -> None:
        self.value = value 
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self) -> None:
        head= None
        tail = None
    def insert(self,value):
        node = Node(value)
        if  self.head =None :
            self.head = node 
        temp = self.head
    def delete(self):
        self.head = self.head.next
        self.head.prev = None 

    def display(self):
        self.head = self.head.next
        self.head.prev = None
    def insertTail(self):
        node =Node(value)
        if self.tail = None or self.head == None:
            self.head = node
            self.tail = node
        self.tail.ext = node

