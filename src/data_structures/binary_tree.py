class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursively(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursively(node.right, value)

    def search(self, value):
        return self._search_recursively(self.root, value)

    def _search_recursively(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursively(node.left, value)
        else:
            return self._search_recursively(node.right, value)

    def print_in_order(self):
        self._print_in_order_recursively(self.root)

    def _print_in_order_recursively(self, node):
        if node is not None:
            self._print_in_order_recursively(node.left)
            print(node.value, end=" ")
            self._print_in_order_recursively(node.right)


# Example usage
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(8)
tree.insert(2)
tree.insert(4)
tree.insert(7)
tree.insert(9)

print("Elements in order:")
tree.print_in_order()

element = 7
found_node = tree.search(element)
if found_node:
    print(f"\nThe element {element} was found in the tree.")
else:
    print(f"\nThe element {element} was not found in the tree.")
