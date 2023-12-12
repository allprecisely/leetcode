# https://leetcode.com/problems/move-zeroes/description/

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index_to_fill = 0
        for num in nums:
            if num != 0:
                nums[index_to_fill] = num
                index_to_fill += 1
        for i in range(index_to_fill, len(nums)):
            nums[i] = 0

