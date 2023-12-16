# https://leetcode.com/problems/leaf-similar-trees/

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.dfs(root1) == self.dfs(root2)

    def dfs(self, root):
        if not root:
            return []
        if not root.right and not root.left:
            return [root.val]
        return self.dfs(root.left) + self.dfs(root.right)

            

            
