# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return None
        le=head
        l=1
        while le.next:
            l=l+1
            le=le.next

        k=k%l
        le.next=head
        temp=head
        for i in range(l-1-k):
            temp=temp.next
        ans=temp.next
        temp.next=None
        return ans
        