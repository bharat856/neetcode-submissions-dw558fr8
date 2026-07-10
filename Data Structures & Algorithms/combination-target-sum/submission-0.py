class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        def backtrack(nums, target, start):
            for i in range(start, len(nums)):
                comb.append(nums[i])
                newTarget = target - nums[i]
                if newTarget == 0:
                    res.append(comb.copy())
                    comb.pop()
                elif newTarget < 0:
                    comb.pop()
                else:
                    backtrack(nums, newTarget, i)
                    comb.pop()
        backtrack(nums, target, 0)
        return res