class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty.")

        min_value = self.heap[0]
        last_value = self.heap.pop()

        if len(self.heap) > 0:
            self.heap[0] = last_value
            self._heapify_down(0)

        return min_value
    
    def remove(self, value):
        if value not in self.heap:
            raise ValueError("Value not found in the heap.")

        # Find the index of the value to remove
        index = self.heap.index(value)

        # Swap the value with the last element
        self.heap[index] = self.heap[-1]
        self.heap.pop()

        # Restore the heap property
        if index < len(self.heap):
            self._heapify_down(index)
            self._heapify_up(index)

    def print_min(self):
        print(self.heap[0])

    def _heapify_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)
            [1, 3, 8, 5]

    def _heapify_down(self, i):
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify_down(smallest)


# Create a MinHeap instance
heap = MinHeap()

# Insert elements
heap.insert(5)
heap.insert(3)
heap.insert(8)
heap.insert(1)
heap.insert(10)

# Extract the minimum element
min_value = heap.extract_min()
print(min_value)  # Output: 1
print()
