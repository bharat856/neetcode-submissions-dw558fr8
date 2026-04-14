class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }
        if len(tokens) == 1 or len(tokens) == 0:
            return int(tokens[0])
        else:
            stk = []
            for item in tokens:
                if item not in operation:
                    stk.append(item)
                else:
                    a = int(stk.pop())
                    b = int(stk.pop())
                    stk.append(operation[item](b,a))
            return stk[-1]
