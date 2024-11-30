class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):  # Allows us to know if the queue is empty
        print (self.items == [])

    def enqueue(self, item):  # Allows us to introduce data into the array 
        self.items.append(item)

    def dequeue(self):  # It cleans the first name give in the array
        self.items.pop(0)

    def size(self):  # Allows us to know the lenght of the array
        print(len(self.items))
    
    def scope(self):  # This prints the whole array
        print(self.items)


   
   
            