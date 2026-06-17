class MinStack:

    def __init__(self):

        self.stack=[]
        self.minStack=[]
        

    def push(self, val: int) -> None:
        
        self.stack.append(val)

        if len(self.minStack) == 0:
            self.minStack.append(val)

        else:
            if self.minStack[-1]<val:
                self.minStack.append(self.minStack[-1])
            else:
                self.minStack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:

        if len(self.stack)>0:
            return self.stack[-1]

        

    def getMin(self) -> int:

        return self.minStack[-1]
        
