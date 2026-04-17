class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        heapq.heapify(minHeap)
        for point in points:
            dist = (0 - point[0])**2 + (0 - point[1])**2
            heapq.heappush(minHeap, (dist, point))
        i = k
        res = []
        while i > 0:
            temp = heapq.heappop(minHeap)
            res.append(temp[1])
            i -= 1
        return res
