# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = list1, list2
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
            
        if l1.val<=l2.val: 
            s = l1 
            l1 = l1.next
        else:
            s = l2
            l2=l2.next
        
        cur = s
        while l1 and l2:
            if l1.val<=l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            
            cur = cur.next
        
        while l1:
            cur.next = l1
            cur = cur.next
            l1 = l1.next
        
        while l2:
            cur.next = l2
            cur = cur.next
            l2 = l2.next

        return s