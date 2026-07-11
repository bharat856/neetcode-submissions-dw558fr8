class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums
        if not nums:
            return 0
        def helper(nums):
            memo = [-1] * len(nums)
            def dp(i):
                if i >= len(nums):
                    return 0
                if memo[i] != -1:
                    return memo[i]
                memo[i] = max(dp(i + 1), nums[i] + dp(i + 2))
                return memo[i]
            return dp(0)
        a = helper(nums[:-1])
        b = helper(nums[1:]) 
        if a > b:
            return a
        return b          
