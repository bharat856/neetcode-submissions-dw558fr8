class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if stk:
                if c in '([{':
                    stk.append(c)
                elif c == ')' and stk[-1] == '(':
                    stk.pop()
                elif c == ']' and stk[-1] == '[':
                    stk.pop()
                elif c == '}' and stack[-1] == '{':
                    stk.pop()
        return not stk