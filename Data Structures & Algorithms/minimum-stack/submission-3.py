class MinStack:

    def __init__(self):
        self.mins = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        new_min = val if not self.mins or self.mins[-1] > val else self.mins[-1]
        self.mins.append(new_min)
        
    def pop(self) -> None:
        self.mins.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

        
    def getMin(self) -> int:
        return self.mins[-1]
        
        
