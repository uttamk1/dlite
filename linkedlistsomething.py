class Node:
    def __init__(self,value) -> None:
        self.value = value 
        self.next = None
        self.prev = None

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
Head = n1
n1.next = n2
n2.next = n3
n3.prev = n2
n2.prev = n1
Tail = n3
while Head!=None:
    print(Head.value,end = "->")
    Head = Head.next
print()

