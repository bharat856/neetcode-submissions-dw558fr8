class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1:
            return [[s]]
        res = []
        charList = list(s)
        def backtrack(currentList, start):
            if start == len(charList):
                res.append(currentList.copy())
                return
            currentWord = ''
            for i in range(start, len(charList)):
                currentWord += charList[i]
                if currentWord == currentWord[::-1]:
                    currentList.append(currentWord)
                    backtrack(currentList, i + 1)
                    #currentWord = currentWord[:-1]
                    currentList.pop()
            return res
        backtrack([], 0)
        return res

