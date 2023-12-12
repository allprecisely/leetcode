# https://leetcode.com/problems/maximum-average-subarray-i/description/

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = 0
        for num in nums[:k]:
            current_sum += num
        
        result = current_sum

        for minus_k_index, num in enumerate(nums[k:]):
            current_sum = current_sum - nums[minus_k_index] + num
            result = max(result, current_sum)
        
        return result / k
