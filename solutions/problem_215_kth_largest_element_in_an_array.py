# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            self.insert(heap, num)
        for _ in range(k):
            result = self.pop(heap)
        return result

    def insert(self, heap: List[int], num: int):
        ind = len(heap)
        heap.append(num)
        while ind:
            parent = (ind - 1) // 2
            if heap[parent] > num:
                break
            heap[parent], heap[ind] = num, heap[parent]
            ind = parent

    def pop(self, heap: List[int]):
        if len(heap) == 1:
            return heap[0]
        result = heap[0]
        heap[0] = heap.pop()
        ind = 0
        while True:
            left_ind, right_ind = ind * 2 + 1, ind * 2 + 2
            if len(heap) > right_ind:
                if heap[ind] > heap[right_ind]:
                    if heap[ind] < heap[left_ind]:
                        heap[ind], heap[left_ind] = heap[left_ind], heap[ind]
                        ind = left_ind
                    else: return result
                elif heap[ind] > heap[left_ind]:
                    heap[ind], heap[right_ind] = heap[right_ind], heap[ind]
                    ind = right_ind
                elif heap[right_ind] > heap[left_ind]:
                    heap[ind], heap[right_ind] = heap[right_ind], heap[ind]
                    ind = right_ind
                else:
                    heap[ind], heap[left_ind] = heap[left_ind], heap[ind]
                    ind = left_ind
            elif len(heap) > left_ind and heap[ind] < heap[left_ind]:
                heap[ind], heap[left_ind] = heap[left_ind], heap[ind]
                ind = left_ind
            else: return result
