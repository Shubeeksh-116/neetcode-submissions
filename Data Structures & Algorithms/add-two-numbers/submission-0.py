# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i1, i2 = "", ""
        while l1:
            i1=str(l1.val)+i1
            l1=l1.next
        while l2:
            i2=str(l2.val)+i2
            l2=l2.next

        res = str(int(i1)+int(i2))
        print(res)
        
        head = t = ListNode(0)
        for i in range(len(res)-1,-1,-1):
            new = ListNode(res[i])
            t.next = new
            t = t.next
        
        return head.next
