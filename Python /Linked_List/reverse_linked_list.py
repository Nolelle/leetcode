from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# returns the head of a linked list
def create_linked_lists(elements):
    dummy_head = ListNode()
    current = dummy_head
    for value in elements:
        current.next = ListNode(value)
        current = current.next
    return dummy_head.next


# recursive solution
class Solution:
    def recursiveReverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not head or not head.next:
            return head
        # recursive case
        reversed_head = self.recursiveReverseList(head.next)
        


obj = Solution()
print(obj.recursiveReverseList(create_linked_lists([1, 2, 3, 4, 5])))
