class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        min_ele = float('inf')
        if self.stack:
            for element in self.stack:
                if element < min_ele:
                    min_ele = element
        
            return min_ele
        else:
            return 0