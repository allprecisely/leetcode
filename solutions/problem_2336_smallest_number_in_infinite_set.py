# https://leetcode.com/problems/smallest-number-in-infinite-set/description/


import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.smallest = 1

    def popSmallest(self) -> int:
        if self.heap and self.smallest > self.heap[0]:
            return heapq.heappop(self.heap)
        self.smallest += 1
        return self.smallest - 1
        

    def addBack(self, num: int) -> None:
        if self.smallest > num and not self.in_heap(num):
            heapq.heappush(self.heap, num)
    
    def in_heap(self, num: int, ind: int = 0) -> bool:
        if len(self.heap) > ind:
            if self.heap[ind] < num:
                return self.in_heap(num, ind * 2 + 1) or self.in_heap(num, ind * 2 + 2)
            if self.heap[ind] == num:
                return True
        return False
