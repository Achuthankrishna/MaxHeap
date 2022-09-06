class Maxheap():
    def __init__ (self,items=[]):
        super(). __init__()
        self.heap=[0]
        for item in items:
            self.heap.append(item)
            self.__floatup(len(self.heap)-1)
    def push(self, data):
        self.heap.append(data)
        self.__floatup(len(self.heap)-1)
    def pop(self):
        if len(self.heap)>2:
            self.__swap(1,len(self.heap)-1)
            max=self.heap.pop()
            self.__bubbledown(1)
        elif len(self.heap)==2:
            max=self.heap.pop()
        else:
            max=False
        return max
    def __swap(self,i,j):
        self.heap[i], self.heap[j]= (self.heap[j],self.heap[i])
    def __floatup(self,index):
        pos=index//2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[pos]:
            self.__swap(index, pos)
            self.__floatup(pos)
    def __bubbledown(self,index):
        left=index*2
        right=index*(2+1)
        largest=index
        if len(self.heap)>left and self.heap[largest]<self.heap[left]:
            largest=left
        if len(self.heap)>right and self.heap[largest]<self.heap[right]:
            largest=right
        if largest != index:
            self.__swap(index,largest)
            self.__bubbledown(largest)
    def __str__(self):
        return str(self.heap)

m=Maxheap([95,3,21])
m.push(101)
print(m)
print(m.pop())