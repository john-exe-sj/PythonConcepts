class Stack:
    def __init__(self):
        self.arr = []

    def is_empty(self): # getter
        return len(self.arr) == 0 # returns a boolean value

    def push(self, num: int): # setter
        if type(num) != int:
            raise ValueError("must be of type int")
        self.arr.append(num)

    def pop(self):
        if not self.is_empty():
            return self.arr.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.arr[-1]
        else:
            raise IndexError("peek from empty stack")
        
    def size(self):
        return len(self.arr)
    






