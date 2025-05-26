# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):    
    def deleteDuplicates(self, head):

        values = []
        before = None
        current = head

        while current:
            if current.val in values:
                before.next = current.next
            else:
                values.append(current.val)
                before = current
            current = current.next
        
        return head
        