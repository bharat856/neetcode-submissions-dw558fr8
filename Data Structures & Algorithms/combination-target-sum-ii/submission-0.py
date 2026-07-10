class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        comb = []
        def backtrack(candidates, target, start):
            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                newTarget = target - candidates[i]
                if newTarget == 0:
                    sorted_comb = sorted(comb)
                    res.add(tuple(sorted_comb))
                    comb.pop()
                elif newTarget < 0:
                    comb.pop()
                else:
                    backtrack(candidates, newTarget, i + 1)
                    comb.pop()
        backtrack(candidates, target, 0)
        return [list(x) for x in res]

                