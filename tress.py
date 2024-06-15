class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None
class Bt:
    def __init__(self):
        self.root = None
    def insert(self,list,index):
        if index >= len(list):
            return None
        root = None
        node = Node(list(index))
        
        root = node
        root.left = self.insert(list,(2*index)+1)
        root.right = self.insert(list,(2*index)+2)
        return root

bt = Bt()
root = bt.insert([5,2,1,9,64],0)
print(root.left.left.value)