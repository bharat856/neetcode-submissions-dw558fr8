class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            memo = [-1] * len(nums)
            def dp(i):
                memo = [0] * len(nums)
                if i >= len(nums):
                    return 0
                if memo[i] != 0:
                    return memo[i]
                memo[i] = max(dp(i + 1), nums[i] + dp(i + 2))
                return memo[i]
            return dp(0)
        a = helper(nums[:-1])
        b = helper(nums[1:]) 
        if a > b:
            return a
        return b          
