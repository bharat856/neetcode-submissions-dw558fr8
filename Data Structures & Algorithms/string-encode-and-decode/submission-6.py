class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for word in strs:
            final += str(len(word))
            for c in word:
                final += c
        return final

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            # Step 1: read the length (it may have more than 1 digit)
            length_str = ""
            while i < len(s) and s[i].isdigit():
                length_str += s[i]
                i += 1
            length = int(length_str)
            # Step 2: read the word of given length
            word = s[i:i + length]
            res.append(word)
            i += length
        return res



