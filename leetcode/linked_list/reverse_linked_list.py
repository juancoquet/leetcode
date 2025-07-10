# https://leetcode.com/problems/reverse-linked-list/description/


from typing import Optional, Self


class ListNode:
    def __init__(self, val: int = 0, next: Optional[Self] = None) -> None:  # noqa: A002
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev, curr = None, head
        while curr.next is not None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        curr.next = prev
        return curr
