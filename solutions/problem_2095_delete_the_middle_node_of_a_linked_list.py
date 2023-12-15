# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None

        size = 0
        node = head
        while node:
            size += 1
            node = node.next
        
        node = head
        for _ in range(size // 2 - 1):
            node = node.next
        
        node.next = node.next.next

        return head