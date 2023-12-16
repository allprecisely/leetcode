# https://leetcode.com/problems/odd-even-linked-list/description/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_head = odd_node = ListNode()
        even_head = even_node = ListNode()
        cur_index = 1
        while head:
            if cur_index % 2 == 0:
                even_node.next = head
                even_node = even_node.next
            else:
                odd_node.next = head
                odd_node = odd_node.next
            head = head.next
            cur_index += 1
        even_node.next = None
        odd_node.next = even_head.next
        return odd_head.next
