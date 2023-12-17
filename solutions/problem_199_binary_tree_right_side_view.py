# https://leetcode.com/problems/binary-tree-right-side-view/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        right_side = []
        level = [root]
        while level:
            right_side.append(level[0].val)
            new_level = []
            for node in level:
                if node.right:
                    new_level.append(node.right)
                if node.left:
                    new_level.append(node.left)
            level = new_level
        return right_side


    def rightSideViewRecursive(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        right = self.rightSideViewRecursive(root.right)
        left = self.rightSideViewRecursive(root.left)
        return [root.val] + right + left[len(right):]
    