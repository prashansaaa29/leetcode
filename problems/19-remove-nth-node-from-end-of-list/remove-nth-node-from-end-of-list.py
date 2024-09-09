# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        l,h=head,head
        for i in range(n):
            h=h.next
        if not h:
            return head.next
        while h.next:
            h=h.next
            l=l.next
        l.next=l.next.next
        return head
        
       
        