# https://leetcode.com/problems/container-with-most-water/description/

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_index, right_index = 0, len(height) - 1
        left_max, right_max = height[left_index], height[right_index]
        result = min(left_max, right_max) * (right_index - left_index)
        while left_index < right_index:
            if left_max < right_max:
                left_index += 1
                if left_max < height[left_index]:
                    left_max = height[left_index]
                    result = max(result, min(left_max, right_max) * (right_index - left_index))
            else:
                right_index -= 1
                if right_max < height[right_index]:
                    right_max = height[right_index]
                    result = max(result, min(left_max, right_max) * (right_index - left_index))
        return result
