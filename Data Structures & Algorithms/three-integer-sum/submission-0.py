class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        l, r = 0, n - 1
        c = 0
        nums.sort()
        res = []
        for c in range(n - 2):
            if c > 0 and nums[c] == nums[c - 1]:
                continue
            l = c + 1
            r = n - 1
            while l < r:
                total = nums[l] + nums[r] + nums[c]
                if  total == 0:
                    res.append([nums[r], nums[l], nums[c]])
                    while l < r and nums[l] == nums[l + 1]:
                        l = l + 1
                    while l < r and nums[r] == nums[r - 1]:
                        r = r - 1
                    l += 1
                    r -= 1 
                elif total < 0:
                    l += 1
                else:
                    r -= 1

        return res