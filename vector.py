import numpy as np

class Vector:
    def __init__(self, name):
        self.name = name # Name for vector
        self.storage = [] # List to store items
        self.vectorStorage = np.array(self.storage) # Convert list to array / vector
        self.options = ["1. Add vectors", "2. Subtract vectors", "3. Multiply vectors", "4. Divide vectors", "5. Calculate dot product", "6. Delete data", "\u001b[31;1m7. Exit.\u001b[0m"]

    def show(self):
        print(f"\u001b[35;1m\nContents for {self.name}:\u001b[0m")
        print(self.storage)

    def showOptions(self):
        print(*self.options, sep=" , ")

    def insertData(self, value):
        self.storage.append(value) # Update list
        self.vectorStorage = np.array(self.storage) # Update array

    def removeData(self, index):
        del self.storage[index] # Update list
        self.vectorStorage = np.array(self.storage) # Update array

    def add(self, secondVector):
        ans = self.vectorStorage + secondVector.vectorStorage
        print("\u001b[35;1m\nResult of addition: %s\u001b[0m" % ans)

    def subtract(self, secondVector):
        ans = self.vectorStorage - secondVector.vectorStorage
        print("\u001b[35;1m\nResult of subtraction: %s\u001b[0m" % ans)
    
    def multiply(self, secondVector):
        ans = self.vectorStorage * secondVector.vectorStorage
        print("\u001b[35;1m\nResult of multiplication: %s\u001b[0m" % ans)

    def divide(self, secondVector):
        ans = self.vectorStorage / secondVector.vectorStorage
        print("\u001b[35;1m\nResult of division: %s\u001b[0m" % ans)

    def dotProduct(self, secondVector):
        ans = self.vectorStorage.dot(secondVector.vectorStorage)
        print("\u001b[35;1m\nDot Product: %s\u001b[0m" % ans)
