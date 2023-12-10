# https://leetcode.com/problems/product-of-array-except-self/description/
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        left_products, right_products = [1] * len_nums, [1] * len_nums
        for i in range(len_nums - 1):
            left_products[i + 1] = left_products[i] * nums[i]
            right_products[i + 1] = right_products[i] * nums[-i - 1]
        return [left_products[i] * right_products[-i - 1] for i in range(len_nums)]