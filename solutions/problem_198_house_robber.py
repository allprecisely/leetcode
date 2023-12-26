# https://leetcode.com/problems/house-robber/description/

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        nums[2] += nums[0]
        for i in range(3, len(nums)):
            nums[i] += max(nums[i - 3], nums[i - 2])
        return max(nums[-1], nums[-2])

