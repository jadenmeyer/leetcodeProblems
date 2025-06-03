"""
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]
Explanation:
Example 2:
Input: head = []
Output: []
Example 3:
Input: head = [1]
Output: [1]
Example 4:
Input: head = [1,2,3]
Output: [2,1,3]
"""
from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        temp = None
        n = None
        while n:
            if curr.next is None:
                return head
            temp = curr
            n = curr.next
            curr = curr.next
            curr = temp
            n = curr.next.next
        g = n
        while g:
            print(g.val)
            g = g.next
        return head

if __name__ == '__main__':
    test = Solution()
    head = ListNode(1)
    n1 = ListNode(2)
    n2 = ListNode(3)
    n3 = ListNode(4)
    head.next = n1
    n1.next = n2
    n2.next = n3
    print(test.swapPairs(head))