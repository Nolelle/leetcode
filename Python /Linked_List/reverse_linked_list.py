from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# iterative solution
class Solution:
    def recursiveReverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp

        return prev
