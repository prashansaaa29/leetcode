# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        curr=head
        for i in range(k):
            if not curr:
                return head
            curr=curr.next
        l=None
        curr=head
        for i in range(k):
            nn=curr.next
            curr.next=l
            l=curr
            curr=nn
        head.next=self.reverseKGroup(curr, k)
        return l

        


        