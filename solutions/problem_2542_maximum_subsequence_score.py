# https://leetcode.com/problems/maximum-subsequence-score/description/

import heapq
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        sorted_nums = sorted(zip(nums2, nums1), reverse=True)
        nums1_sum_heap = []
        nums1_sum = 0
        for _, num1 in sorted_nums[:k]:
            heapq.heappush(nums1_sum_heap, num1)
            nums1_sum += num1
        result = sorted_nums[k - 1][0] * nums1_sum
        for num2, num1 in sorted_nums[k:]:
            if num1 > nums1_sum_heap[0]:
                nums1_sum += num1 - heapq.heappushpop(nums1_sum_heap, num1)
                result = max(result, nums1_sum * num2)
        return result
