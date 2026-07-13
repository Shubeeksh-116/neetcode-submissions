# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = []
        c = head
        while c:
            s.append(c)
            c=c.next
        
        print(s)
        
        l,r = 0, len(s)-1
        
        st = s[l]
        while l<r:
            n = s[l].next
            s[l].next = s[r]
            s[r].next = n
            l+=1
            r-=1
        s[l].next=None
        