# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/


from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ancestor = None
        self.dfs(root, [p, q])
        return self.ancestor

    def dfs(self, root: 'TreeNode', not_found: List['TreeNode']) -> List['TreeNode']:
        if root == None or self.ancestor != None:
            return []

        found = self.dfs(root.left, not_found) + self.dfs(root.right, not_found)
        if root in not_found:
            found.append(root)
        if self.ancestor == None and set(found) == set(not_found):
            self.ancestor = root
        return found
