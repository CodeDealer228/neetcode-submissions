from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        if not len(tokens): 
            return 0
        for tok in tokens:
            if tok not in '+-*/':
                stack.append(int(tok))
            else:
                b = stack.pop()
                a = stack.pop()
                if tok == '+':
                    c = a + b
                elif tok == '-':
                    c = a - b
                elif tok == '*':
                    c = a * b
                else:
                    c = int(a / b)
                stack.append(c)
        return stack.pop()
