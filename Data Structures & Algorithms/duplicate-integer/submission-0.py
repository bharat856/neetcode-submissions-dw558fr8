class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = set(nums)
        return not (len(x) == len(nums))