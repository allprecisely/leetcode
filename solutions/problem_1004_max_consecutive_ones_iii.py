# https://leetcode.com/problems/max-consecutive-ones-iii/description/

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for num in nums:
            if num == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        return len(nums) - left