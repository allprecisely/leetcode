# https://leetcode.com/problems/find-peak-element/description/

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if middle == len(nums) or nums[middle] > nums[middle + 1]:
                if middle == 0 or nums[middle] > nums[middle - 1]:
                    return middle
                right = middle
            else: left = middle + 1
        return left
