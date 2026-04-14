class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = 0
        res = []

        while l < len(temperatures):
            found = False

            for r in range(l + 1, len(temperatures)):
                if temperatures[r] > temperatures[l]:
                    res.append(r - l)
                    found = True
                    break

            if not found:
                res.append(0)

            l += 1

        return res