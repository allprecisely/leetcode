# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        level_num = result = 0
        levels = [root]
        while levels:
            level_num += 1
            new_levels = []
            level_max_sum = 0
            for level in levels:
                level_max_sum += level.val
                if level.left:
                    new_levels.append(level.left)
                if level.right:
                    new_levels.append(level.right)
            levels = new_levels
            if level_max_sum > max_sum:
                max_sum = max(max_sum, level_max_sum)
                result = level_num

        return result
