class Solution:
    def encode(self, strs: List[str]) -> str:
            res = []
            for s in strs:
                res.append('#' + str(len(s)) + s)
            a = ''.join(res)
            return a
    def decode(self, s: str) -> List[str]:
            res = []
            i = 0
            while i < len(s):
                if s[i] == '#':
                    lenWord = int(s[i + 1])
                    res.append(s[i+2: lenWord + i + 2])
                    i = lenWord + i + 1
                else:
                    i += 1
            return res






