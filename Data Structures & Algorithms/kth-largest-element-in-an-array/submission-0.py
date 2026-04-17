class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for i in range(len(nums)):
            nums[i] = -1 * nums[i]
        maxHeap = nums
        heapq.heapify(maxHeap)
        j = k
        while j > 0:
            a = heapq.heappop(maxHeap)
            j -= 1
        return -1*a
