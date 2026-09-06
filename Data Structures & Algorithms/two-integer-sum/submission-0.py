class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in nums[i:]:
                res.append(i)
                res.append(nums.index(rem))
            return res