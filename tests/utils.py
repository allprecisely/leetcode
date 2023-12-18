from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        left = self.left.val if self.left else None
        right = self.right.val if self.right else None
        return f'\'Node ({self.val}): left={left}, right={right}\''


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


def list_to_tree(vals: List[int]) -> Optional[TreeNode]:
    if not vals:
        return None
    
    head = TreeNode(vals[0])
    nodes = deque([head])

    left = True
    for val in vals[1:]:
        node = TreeNode(val) if val != None else None
        if left:
            nodes[0].left = node
            left = False
        else:
            nodes.popleft().right = node
            left = True
        if node:
            nodes.append(node)

    return head


def find_node(root: Optional[TreeNode], val: int) -> TreeNode:
    if root != None:
        if root.val == val:
            return root
        return find_node(root.left, val) or find_node(root.right, val)