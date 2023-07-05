class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def delete(self, data):
        if self.is_empty():
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        if self.is_empty():
            print("LinkedList is empty.")
        else:
            current = self.head
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")


# Create a new LinkedList
my_list = LinkedList()

# Append elements to the LinkedList
my_list.append(5)
my_list.append(10)
my_list.append(15)

# Prepend an element to the LinkedList
my_list.prepend(1)

# Display the LinkedList
my_list.display()  # Output: 1 -> 5 -> 10 -> 15 -> None

# Delete an element from the LinkedList
my_list.delete(10)

# Display the updated LinkedList
my_list.display()  # Output: 1 -> 5 -> 15 -> None
