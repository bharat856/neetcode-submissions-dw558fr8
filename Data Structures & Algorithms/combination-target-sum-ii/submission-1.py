from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        comb = []

        def backtrack(target, start):
            if target == 0:
                res.append(comb.copy())
                return

            for i in range(start, len(candidates)):
                # Skip duplicates at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Stop early because array is sorted
                if candidates[i] > target:
                    break

                comb.append(candidates[i])
                backtrack(target - candidates[i], i + 1)
                comb.pop()

        backtrack(target, 0)
        return res