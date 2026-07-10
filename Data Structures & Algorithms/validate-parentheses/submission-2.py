class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 1:
            return False
        else:
            for c in s:
                if c in '([{':
                    stack.append(c)
                elif c == ')' and stack[-1] == '(':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
            return not stack