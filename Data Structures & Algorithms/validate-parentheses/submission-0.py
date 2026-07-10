class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
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