# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first_biggest = second_biggest = 1
        for num in nums:
            if num > first_biggest:
                first_biggest, second_biggest = num, first_biggest
            elif num > second_biggest:
                second_biggest = num
        return (first_biggest - 1) * (second_biggest - 1)
