class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s1 = sorted(s)
        t1 = sorted(t)
        return s1 == t1
