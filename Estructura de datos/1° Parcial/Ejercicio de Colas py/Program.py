class Program:
    def __init__(self):
        self.items = []

    def isEmpty(self):  
        print (self.items == [])

    def enqueue(self, item): 
        self.items.append(item)

    def dequeue(self):  
        self.items.pop(0)

    def size(self): 
        print(len(self.items))
    
    def scope(self):
        print(self.items)


   
            