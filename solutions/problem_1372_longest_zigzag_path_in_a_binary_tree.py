# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0, 0, True)

    def dfs(self, root: Optional[TreeNode], left: int, right: int, is_left: bool) -> int:
        if root == None:
            return left + right - 1
        
        if is_left:
            return max(self.dfs(root.left, 1, 0, True), self.dfs(root.right, left, right + 1, False))
        else:
            return max(self.dfs(root.left, left + 1, right, True), self.dfs(root.right, 0, 1, False))
