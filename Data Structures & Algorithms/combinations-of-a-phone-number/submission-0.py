class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        num_to_char = {
            '2':'abc', '3':'def', '4': 'ghi',
            '5':'jkl', '6':'mno', '7': 'pqrs',
            '8':'tuv', '9':'wxyz'
            }
        res = []
        def backtrack(requiredCombinations, currentString):
            if len(requiredCombinations) == len(currentString):
                res.append(currentString)
                return
            index = len(currentString)
            for c in requiredCombinations[index]:
                currentString += c
                backtrack(requiredCombinations, currentString)
                currentString = currentString[:-1]
        
                

        
        requiredCombinations = []
        for digit in digits:
            requiredCombinations.append(num_to_char[digit])
        backtrack(requiredCombinations, '')
        return res