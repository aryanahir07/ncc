class PriorityQueue:

    def __init__(self):
        self.queue=[]

    def enqueue(self,item,priority):
        element=(item,priority)
        self.queue.append(element)
        self.queue.sort(key=lambda x: x[1])

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)[0]
        else:
            return None

    def is_empty(self):
        return len(self.queue)==0

priority_queue = PriorityQueue()
priority_queue.enqueue("Task 1",4)
priority_queue.enqueue("Task 2",2)
priority_queue.enqueue("Task 3",3)
priority_queue.enqueue("Task 4",1)
while not priority_queue.is_empty():
    print(priority_queue.dequeue())