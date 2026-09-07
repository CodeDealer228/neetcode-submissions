from collections import deque

class Solution:
    def __init__(self):
        self.operations = '+-*/'
        self.eps = 1e-8

    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        if not len(tokens): 
            return 0
        for tok in tokens:
            if tok not in self.operations:
                stack.append(int(tok))
            else:
                b = stack.pop()
                a = stack.pop()
                if tok == '+':
                    stack.append(a + b)
                elif tok == '-':
                    stack.append(a - b)
                elif tok == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
        return stack.pop()
