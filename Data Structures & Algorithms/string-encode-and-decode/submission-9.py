class Solution:
    def encode(self, strs: List[str]) -> str:
            res = []
            for s in strs:
                res.append(str(len(s)) + '#' + s)
            a = ''.join(res)
            return a
    def decode(self, s: str) -> List[str]:
            res = []
            i = 0
            while i < len(s):
                j = i
                while s[j] != '#':
                    j += 1
                lenWord = int(s[i:j])
                res.append(s[j + 1: lenWord + j + 1])
                i = lenWord + j + 1
            return res






