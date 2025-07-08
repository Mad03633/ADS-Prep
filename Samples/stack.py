# Python implementations of stacks - List-based implementation and Deque-based implementation 

class ListBasedStack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("pop from empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("peek from empty stack")
    
    def is_empty(self):
        return len(self.stack) == 0
    

from collections import deque

class DequeBasedStack:
    def __init__(self):
        self.stack = deque()
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("pop from empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("peek from empty stack")
    
    def is_empty(self):
        return len(self.stack) == 0

if __name__ == "__main__":
    stack = ListBasedStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.peek())  # 3
    print(stack.pop())   # 3
    print(stack.peek())  # 2
    print(stack.pop())   # 2
    print(stack.peek())  # 1
    print(stack.pop())   # 1
    print(stack.is_empty())  # True

    stack = DequeBasedStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.peek())  # 3
    print(stack.pop())   # 3
    print(stack.peek())  # 2
    print(stack.pop())   # 2
    print(stack.peek())  # 1
    print(stack.pop())   # 1
    print(stack.is_empty())  # True
