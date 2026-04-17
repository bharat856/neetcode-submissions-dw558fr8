class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -1 * stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            a = -1*heapq.heappop(stones)
            b = -1*heapq.heappop(stones)
            if a == b:
                continue
            elif a > b:
                heapq.heappush(stones,(-1 * (a - b)))
            else:
                heapq.heappush(stones, (-1 * (b - a)))
        return -1 * stones[0] if stones else 0