# given an integre k and queue of integrs , we need to reverse the oder of the first k elements of queue, leaving other elements in same order.
# only the fo]llowing operation are alloed
# enque(x) add item to rear of Queue
# dequeu():remove item from front of qu
# size() returns nimebr of elements in Queue
# front() finds front leemkdng



# class Queue:
#     def __init__(self) -> None:
#          self.stack =[]
#     def Enqueue(self,value):
#     self.stack.append(value)
#     def Dequeue(self):
#         self.temp = self.stack[1:]
#         self.temp = self.temp[::-1]
#         value = self.stack[len(self.stack)-1]
#         self.stack.clear()
#         self.stack = self.temp[::-1]
#         return value

def RotateQueue(queue,k):
    tempQueue = []
    stack = []
    for i in range(k):
        stack.append(queue.pop(0))
    
    for i in range(k):
        tempQueue.append(stack.pop())
    for i in queue:
        tempQueue.append(i)
    print(tempQueue)


queue = [1,2,3,4,5]
k = 3
RotateQueue(queue,k)