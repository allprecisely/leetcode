from typing import Dict, List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# full tree
def tree_to_list(root: TreeNode) -> List[int]:
    def helper(node: TreeNode, level: int = 0) -> Dict[int, List[int]]:
        if not node:
            return {}
        left_levels = helper(node.left, level + 1)
        right_levels = helper(node.right, level + 1)
        for k, v in right_levels.items():
            left_levels[k] += v
        return {**left_levels, level: [node.val]}
    
    result = []
    levels = helper(root)
    for i in range(len(levels)):
        result += levels[i]
    return result


# full tree
def list_to_tree(vals: List[int]) -> Optional[TreeNode]:
    if not vals:
        return None
    nodes = [TreeNode(val) if val else None for val in vals]
    for i in range(1, len(vals)):
        parent_index = (i - 1) // 2
        if nodes[parent_index]:
            if i % 2:
                nodes[parent_index].left = nodes[i]
            else:
                nodes[parent_index].right = nodes[i]
    return nodes[0]

"""
         0
    1           2
  3   4      5     6
 7 8 9 10  11 12 13 14
"""