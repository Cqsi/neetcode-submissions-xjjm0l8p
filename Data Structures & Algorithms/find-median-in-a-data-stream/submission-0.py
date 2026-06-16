import heapq

class MedianFinder:

    def __init__(self):
        self.minHeap = [] # "right" heap
        self.maxHeap = [] # "left" heap

    def addNum(self, num: int) -> None:

        minHeap = self.minHeap
        maxHeap = self.maxHeap

        if len(minHeap) == 0 and len(maxHeap) == 0:
            heapq.heappush(minHeap, num)
            return

        if num > minHeap[0]:
            heapq.heappush(minHeap, num)
            if len(minHeap) - len(maxHeap) > 1:
                e = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, -e)
        else:
            heapq.heappush(maxHeap, -num)
            if len(maxHeap) - len(minHeap) > 1:
                e = heapq.heappop(maxHeap)
                heapq.heappush(minHeap, -e)

    def findMedian(self) -> float:

        minHeap = self.minHeap
        maxHeap = self.maxHeap

        if len(minHeap) == len(maxHeap):
            return (-maxHeap[0] + minHeap[0])/2
        elif len(minHeap) > len(maxHeap):
            return minHeap[0]
        else:
            return -maxHeap[0]
        