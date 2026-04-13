class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a = set(s1)
        b = set(s2)
        if len(s2) < len(s1):
            return False
        n = len(s1)
        for l in range(len(s2) - n + 1):
            if s2[l] in a:
                if sorted(s2[l:l+n]) == sorted(s1):
                    return True
        return False