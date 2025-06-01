from operator import truediv
from typing import List, Optional
"""Given the head of a singly linked list, return true if it is a palindrome or false otherwise."""


# Definition for singly-linked list.
#Input: head = [1,2,2,1]
#Output: true
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        copy = head
        node1 = self.copyList(copy)
        node2 = self.reverse(copy)
        while node1 and node2:
            if node1.val != node2.val:
                return False
            node1 = node1.next
            node2 = node2.next
        return True

    def reverse(self, torev: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = torev
        next = torev

        while curr:
            next = next.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def copyList(self, toCopy: Optional[ListNode]) -> Optional[ListNode]:
        new_node = ListNode(toCopy.val)
        curr_old = toCopy.next
        curr_new = new_node
        while curr_old is not None:
            curr_new.next = ListNode(curr_old.val)
            curr_old = curr_old.next
            curr_new = curr_new.next
        return new_node

if __name__ == '__main__':
    test = Solution()
    """head = ListNode(1)
    n1 = ListNode(2)
    n2 = ListNode(2)
    n3 = ListNode(1)
    head.next = n1
    n1.next = n2
    n2.next = n3
    tail = ListNode(1)
    nn = ListNode(2)
    tail.next = nn"""
    #[1,1,2,1]
    head1 = ListNode(1)
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(1)
    head1.next = n1
    n1.next = n2
    n2.next = n3
    test2 = head1
    while test2:
        #print(test2.val)
        test2 = test2.next
    print(test.isPalindrome(head1))
    #print(test.isPalindrome())
    #print("test")

"""
horrible solution but runtime of 5%
"""