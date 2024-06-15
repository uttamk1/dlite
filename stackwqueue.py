class Queue:
    def __init__(self) -> None:
        self.stack = []
        self.temp = []
    def Enqueue(self,value):
        self.stack.append(value)
    def Dequeue(self):
        self.temp = self.stack[1:]
        self.temp = self.temp[::-1]
        value = self.stack[len(self.stack)-1]
        self.stack.clear()
        self.stack = self.temp[::-1]
        return value
q = Queue()
for i in [10,25,30,45,39]:
    q.Enqueue(i)
print(q.stack)
q.Dequeue()
print(q.stack)