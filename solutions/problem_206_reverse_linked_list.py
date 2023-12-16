# https://leetcode.com/problems/reverse-linked-list/description/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = None
        while head:
            child = head.next
            head.next = tail
            tail = head
            head = child
        return tail
