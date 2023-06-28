class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty.")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Queye is empty.")

    def size(self):
        return len(self.queue)


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.peek())  # Output: 1
print(queue.dequeue())   # Output: 1
print(queue.size())  # Output: 2
