'''
Three approaches:
1) Create a stack that stores a tuple containing the value pushed + the curMin
2) Create two stacks
    - StackA contains the values pushed
    - StackB contains the curMin that get pushed onto the stack if they are less than or equal to the curMin
3) Create two stacks (improved)
    - StackA contains the values pushed
    - StackB contains the minimum values up to that point, and how many times that minimum value has occurred up to that point
'''

from collections import deque

class MinStack(object):
    def __init__(self):
        self.elements = deque()
        self.minimums = deque()

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.elements.append(val)
        if len(self.minimums) == 0:
            self.minimums.append(val)
        elif val <= self.minimums[-1]:
            self.minimums.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        if self.elements.pop() == self.minimums[-1]:
            self.minimums.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.elements[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minimums[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    min = minStack.getMin() # return -3
    print(f"min = {min}")
    minStack.pop()
    top = minStack.top()    # return 0
    min = minStack.getMin() # return -2
    print(f"top = {top}")
    print(f"min = {min}")
 