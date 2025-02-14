# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        temp=head
        stack=[]
        while temp!=None:
            stack.append(temp.val)
            temp=temp.next
        temp=head
        while len(stack)!=0:
            if temp.val!=stack.pop():
                return False
            temp=temp.next
        return True

        