"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return head
        otn={}
        curr=head
        while curr:
            otn[curr]=Node(curr.val)
            curr=curr.next
        curr=head
        while curr:
            otn[curr].next=otn.get(curr.next)
            otn[curr].random=otn.get(curr.random)
            curr=curr.next
        return otn[head]









'''class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        old_to_new = {}
        
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next
            
        return old_to_new[head]'''

        