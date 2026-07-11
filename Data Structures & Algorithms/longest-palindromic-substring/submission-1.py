class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        leftIndex = 0
        rightIndex = 0
        def dp(left, right):
            nonlocal maxLen, leftIndex, rightIndex
            if left >= right:
                return
            if s[left:right + 1] == s[left:right + 1][::-1]:
                if maxLen < (right - left + 1):
                    maxLen = (right - left + 1)
                    leftIndex = left
                    rightIndex = right
            dp(left, right - 1)
            dp(left + 1, right)
            dp(left + 1, right - 1)

        dp(0, len(s) - 1)
        return s[leftIndex : rightIndex + 1]