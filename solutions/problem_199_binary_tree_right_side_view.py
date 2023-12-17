# https://leetcode.com/problems/binary-tree-right-side-view/

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root]) if root else None
        right_side = []
        level_size, next_level_size = 1, 0
        while queue:
            node = queue.popleft()
            level_size -= 1
            if node.left:
                queue.append(node.left)
                next_level_size += 1
            if node.right:
                queue.append(node.right)
                next_level_size += 1
            if level_size == 0:
                right_side.append(node.val)
                level_size, next_level_size = next_level_size, 0
        return right_side
