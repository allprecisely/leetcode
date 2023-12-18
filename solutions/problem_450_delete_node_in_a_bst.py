# https://leetcode.com/problems/delete-node-in-a-bst/description/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif root.left and root.right:
            child = root.right
            while child.left:
                child = child.left
            root.val = child.val
            root.right = self.deleteNode(root.right, root.val)
        else:
            return root.left or root.right

        return root
