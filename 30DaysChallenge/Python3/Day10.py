class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = [] 
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        
        if len(self.minStack) > 0:
            self.minStack.append(min(self.minStack[-1],x))
        else:
            self.minStack.append(x)

    def pop(self) -> None:
        if len(self.stack) == 0:
            raise Exception("")
    
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return 0
        

    def getMin(self) -> int:
        if len(self.minStack) > 0:
            return self.minStack[-1]
        else:
            return -float("inf")
            
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()