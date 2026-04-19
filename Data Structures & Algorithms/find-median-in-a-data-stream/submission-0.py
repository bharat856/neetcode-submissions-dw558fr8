class MedianFinder:

    def __init__(self):
        self.numList = []

    def addNum(self, num: int) -> None:
        self.numList.append(num)

    def findMedian(self) -> float:
        self.numList.sort()
        n = len(self.numList)
        return (self.numList[n // 2] if (n & 1) else
                (self.numList[n // 2] + self.numList[n // 2 - 1]) / 2)