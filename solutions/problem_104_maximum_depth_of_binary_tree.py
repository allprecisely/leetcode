# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    def maxDepthIterable(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        queue = deque([root])
        queue_length = 1
        levels = 0
        while queue:
            node = queue.popleft()
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.append(node.right)
            queue_length -= 1
            print(queue, node, queue_length)
            if queue_length == 0:
                levels += 1
                queue_length = len(queue)
        return levels
