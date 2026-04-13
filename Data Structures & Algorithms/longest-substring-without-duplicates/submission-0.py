class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0
        window = 0
        left = 0
        n = len(s)
        seen = set()
        while window < n:
            if s[window] not in seen:
                seen.add(s[window])
                maxL = max(maxL, len(seen))
                window += 1
            else:
                seen.remove(s[left])
                left += 1
        return maxL
