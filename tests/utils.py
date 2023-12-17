from collections import deque
from typing import Dict, List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# full tree
def tree_to_list(root: TreeNode) -> List[int]:
    tree_list = []
    queue = deque([root]) if root else None
    while queue:
        node = queue.popleft()
        if node:
            queue.append(node.left)
            queue.append(node.right)
        tree_list.append(node.val if node else None)
        
    while tree_list and tree_list[-1] == None:
        tree_list.pop()
    return tree_list


# full tree
def list_to_tree(vals: List[int]) -> Optional[TreeNode]:
    if not vals:
        return None
    
    head = TreeNode(vals[0])
    nodes = deque([head])

    left = True
    for val in vals[1:]:
        node = TreeNode(val) if val else None
        if left:
            nodes[0].left = node
            left = False
        else:
            nodes.popleft().right = node
            left = True
        if node:
            nodes.append(node)

    return head

"""
         0
    1           2
  3   4      5     6
 7 8 9 10  11 12 13 14
"""