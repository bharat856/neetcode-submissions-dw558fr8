class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        for num in nums:
            if num  not in seen:
                seen.append(num)
            elif num in seen:
                return True
        return False