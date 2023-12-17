# https://leetcode.com/problems/path-sum-iii/description/

from typing import Dict, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return self.dfs(root, targetSum, 0, {targetSum: 1})

    def dfs(self, root: Optional[TreeNode], target_sum: int, parent_sum: int, target_sums: Dict[int, int]) -> int:
        if not root:
            return 0

        result = 0
        
        current_sum = parent_sum + root.val
        current_sum_with_target = current_sum + target_sum
        result += target_sums.get(current_sum, 0)
        target_sums[current_sum_with_target] = target_sums.get(current_sum_with_target, 0) + 1
        
        result += self.dfs(root.left, target_sum, current_sum, target_sums)
        result += self.dfs(root.right, target_sum, current_sum, target_sums)
        target_sums[current_sum_with_target] -= 1
        return result
