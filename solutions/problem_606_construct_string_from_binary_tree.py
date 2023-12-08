# https://leetcode.com/problems/construct-string-from-binary-tree/description/
# 1 try
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root.left and root.right:
            return f'{root.val}({self.tree2str(root.left)})({self.tree2str(root.right)})'
        if root.left:
            return f'{root.val}({self.tree2str(root.left)})'
        if root.right:
            return f'{root.val}()({self.tree2str(root.right)})'
        return str(root.val)
