# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        parents = []
        visited = set()
        while True:
            if root.left and root.left not in visited:
                parents.append(root)
                root = root.left
            elif root.right and root.right not in visited:
                result.append(root.val)
                visited.add(root)
                parents.append(root)
                root = root.right
            else:
                if not root in visited:
                    result.append(root.val)
                    visited.add(root)
                if not parents:
                    return result
                root = parents.pop()
