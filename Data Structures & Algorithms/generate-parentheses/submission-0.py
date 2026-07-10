class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        currentString = ''
        res = []
        if n == 1:
            return ['()']
        def backtrack(currentString, openCount, closeCount):
            if openCount == n and closeCount == n:
                res.append(currentString)
                return res
            if openCount < n:
                currentString += '('
                backtrack(currentString, openCount + 1, closeCount)
                currentString = currentString[:-1]
            if openCount > closeCount:
                currentString += ')'
                backtrack(currentString, openCount, closeCount + 1)
                currentString = currentString[:-1]
        backtrack(currentString, 0, 0)
        return res

