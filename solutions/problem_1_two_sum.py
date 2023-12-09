# https://leetcode.com/problems/two-sum/
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set_nums = set(nums)
        first_index = None
        for num in set_nums:
            if target - num in set_nums:
                if num == target - num:
                    for i, _num in enumerate(nums):
                        if num == _num:
                            if first_index == None:
                                first_index = i
                            else:
                                return [first_index, i]
                    first_index = None
                else:
                    return [nums.index(num), nums.index(target - num)]
