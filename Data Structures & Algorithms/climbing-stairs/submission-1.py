class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        def backtrack(current_step):
            nonlocal count
            if current_step == n:
                count += 1
                return
            if current_step > n:
                return
            backtrack(current_step + 1)
            backtrack(current_step + 2)
        backtrack(0)
        return count