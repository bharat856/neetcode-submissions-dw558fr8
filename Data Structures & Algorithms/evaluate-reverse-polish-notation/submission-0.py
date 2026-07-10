class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b
        }
        stk = []
        for item in tokens:
            if item not in operation:
                stk.append(item)
            else:
                a = int(stk.pop())
                b = int(stk.pop())
                stk.append(operation[item](a,b))
        return stk[-1]
