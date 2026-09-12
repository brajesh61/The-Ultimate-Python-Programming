# Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.

class Node:
    """Class to represent a node in the Binary Search Tree."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    """Class to represent a Binary Search Tree."""
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a new key into the BST."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        """Helper method to insert a new key recursively."""
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_recursive(current_node.left, key)
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_recursive(current_node.right, key)
        else:
            # Duplicate values are not inserted in BST
            print(f"Key {key} already exists in the BST.")

    def search(self, key):
        """Search for a key in the BST. Returns True if found, else False."""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current_node, key):
        """Helper method to search for a key recursively."""
        if current_node is None:
            return False
        if key == current_node.key:
            return True
        elif key < current_node.key:
            return self._search_recursive(current_node.left, key)
        else:
            return self._search_recursive(current_node.right, key)


# Example usage

bst = BinarySearchTree()
bst.insert(50)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print(bst.search(40))  # True
print(bst.search(100))  # False
