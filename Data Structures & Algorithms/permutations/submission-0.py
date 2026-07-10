class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        comb = []
        def backtrack(nums):
            for i in range(len(nums)):
                comb.append(nums[i])
                remainingPass = nums[:i] + nums[i+1:]
                if not remainingPass:
                    res.append(comb.copy())
                backtrack(remainingPass)
                comb.pop()
            return res
        return backtrack(nums)