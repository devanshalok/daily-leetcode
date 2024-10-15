class MinStack:

    def __init__(self):
        # Initialize the Stack and Minstack
        self.stack=[]
        self.minstack=[]
        

    def push(self, val: int) -> None:
        # Append the value to stack
        self.stack.append(val) 
        # See if the incomin value is less than the top of the stack or the array is empty
        if not self.minstack or val<self.minstack[-1]:
            self.minstack.append(val)

        else:
            # Append the last value that is also the minimum of all the values that came
            self.minstack.append(self.minstack[-1])
        

    def pop(self) -> None:
        # simple pop from both the stacks
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        # Top of the stack 
        return self.stack[-1]
        
    def getMin(self) -> int:
        # This is actually from the top for append the value in minstack 
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()