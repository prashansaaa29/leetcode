# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow=head
        f=head
        while f and f.next:
            slow=slow.next
            f=f.next.next
            if slow is f:
                start=head
                while start is not slow:
                    start=start.next
                    slow=slow.next
                return start
        return None
        