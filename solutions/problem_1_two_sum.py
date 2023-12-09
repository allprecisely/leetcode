# https://leetcode.com/problems/two-sum/
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_indexes = {}
        for i, num in enumerate(nums):
            if target - num in nums_indexes:
                return [i, nums_indexes[target - num]]
            nums_indexes[num] = i
