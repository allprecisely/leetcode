# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        node = head
        second_half_node = head
        while node and node.next:
            node = node.next.next
            second_half_node = second_half_node.next
        
        second_half_reversed_head = None
        while second_half_node:
            tail = second_half_node.next
            second_half_node.next = second_half_reversed_head
            second_half_reversed_head = second_half_node
            second_half_node = tail
        
        result = 0
        while second_half_reversed_head:
            result = max(result, head.val + second_half_reversed_head.val)
            head, second_half_reversed_head = head.next, second_half_reversed_head.next
        
        return result 
