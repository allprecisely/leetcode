# https://leetcode.com/problems/product-of-array-except-self/description/
# 1 try; but not memory optimal, so improved
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        answer = [1] * len_nums
        left_product = right_product = 1
        for i in range(len_nums):
            answer[i] *= left_product
            left_product *= nums[i]
            answer[-i - 1] *= right_product
            right_product *= nums[-i - 1]
        return answer
        