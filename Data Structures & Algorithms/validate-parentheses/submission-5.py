class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeDict = {')':'(', ']':'[', '}': '{'}

        for c in s:
            if c in closeDict:
                if stack and stack[-1] == closeDict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False