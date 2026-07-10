class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        temp1 = sorted(set(s))
        temp2 = sorted(set(t))
        return temp1 == temp2