# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)

    def dfs(self, root: TreeNode, max_in_path: int) -> int:
        if root == None:
            return 0
        if root.val >= max_in_path:
            return 1 + self.dfs(root.left, root.val) + self.dfs(root.right, root.val)
        else:
            return self.dfs(root.left, max_in_path) + self.dfs(root.right, max_in_path)
