class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        leftIndex = 0
        rightIndex = 0
        visited = set()
        def dp(left, right):
            nonlocal maxLen, leftIndex, rightIndex
            while left <= right:
                if (left, right) in visited:
                    return
                visited.add((left, right))
                if s[left:right + 1] == s[left:right + 1][::-1]:
                    if maxLen < (right - left + 1):
                        maxLen = (right - left + 1)
                        leftIndex = left
                        rightIndex = right
                        
                dp(left + 1, right)
                right -= 1

        dp(0, len(s) - 1)
        return s[leftIndex : rightIndex + 1]