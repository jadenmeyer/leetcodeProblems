from typing import List, Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None #if a node will print a null value
        next = head

        while curr:
            next = next.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

if __name__ == '__main__':
    print("hi")