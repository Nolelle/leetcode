from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def lengthOfLinkedList(self, head: Optional[ListNode]) -> int:
        curr = head
        count = 0

        while curr:
            curr = curr.next
            count += 1

        return count

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        n = self.lengthOfLinkedList(head)
        count = 0

        if not head or not head.next:
            return None
        if n == 1 or n == 2:
            return head.next

        while count < n // 2 - 1:
            count += 1
            curr = curr.next

        curr.next = curr.next.next

        return head
