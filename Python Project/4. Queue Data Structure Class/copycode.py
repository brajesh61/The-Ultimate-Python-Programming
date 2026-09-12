# Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.

# Define a class called Queue to implement a queue data structure
class Queue:
    # Initialize the queue with an empty list to store items
    def __init__(self):
        self.items = []

    # Add (enqueue) an item to the end of the queue
    def enqueue(self, item):
        self.items.append(item)

    # Remove and return (dequeue) an item from the front of the queue if the queue is not empty
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Cannot dequeue from an empty queue.")

    # Check if the queue is empty
    def is_empty(self):
        return len(self.items) == 0

# Example usage
# Create an instance of the Queue class
queue = Queue()

# Enqueue (add) items to the queue
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

# Print the current items in the queue
print("Current Queue:", queue.items)

# Dequeue (remove) items from the front of the queue and print the dequeued items
# dequeued_item = queue.dequeue()
# print("Dequeued item:", dequeued_item)
# dequeued_item = queue.dequeue()
# print("Dequeued item:", dequeued_item)

# # Print the updated items in the queue
# print("Updated Queue:", queue.items) 
