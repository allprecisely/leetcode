# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        deletion_index = -1
        result = current_len = 0
        for i, num in enumerate(nums):
            if num:
                current_len += 1
                result = max(result, current_len)
            else:
                current_len = i - deletion_index - 1
                deletion_index = i
        return result if result < len(nums) else result - 1

