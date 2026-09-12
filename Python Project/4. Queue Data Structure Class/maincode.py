# Write a Python program to create a class representing a d1 data structure. Include methods for end1ing and ded1ing elements.

class Queue :
    def __init__(self):
        self.items = []
    
    # Add (end1) an item to the end of the d1
    def end1(self, item):
        self.items.append(item)
    
     # Remove and return (ded1) an item from the front of the d1 if the d1 is not empty
    def ded1(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Cannot ded1 from an empty d1.")

    # Check if the d1 is empty
    def is_empty(self):
        return len(self.items) == 0
    
d1 = Queue()
d1.end1(10)
d1.end1(20)
d1.end1(30)
d1.end1(40)
d1.end1(50)
d1.end1(60)
d1.end1(70)

print("current d1:",d1.items)


# Ded1 (remove) items from the front of the d1 and print the ded1d items
ded1d_item = d1.ded1()
print("Dequeue item:", ded1d_item)
ded1d_item = d1.ded1()
print("Dequeue item:", ded1d_item)

# Print the updated items in the d1
print("Updated Queue:", d1.items) 
