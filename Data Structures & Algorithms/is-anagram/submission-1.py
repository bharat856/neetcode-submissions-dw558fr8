class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        temp1 = sorted(s)
        temp2 = sorted(t)
        return temp1 == temp2