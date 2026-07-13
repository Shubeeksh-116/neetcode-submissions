"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = {}
        cur = head
        new_head = new_cur = Node(0)
        while cur:
            temp = Node(cur.val)
            new_cur.next = temp
            d[cur]=temp
            cur=cur.next
            new_cur=new_cur.next
        
        new_head = new_cur = new_head.next
        cur = head

        while new_cur:
            if cur.random:
                new_cur.random = d[cur.random]
            cur=cur.next
            new_cur=new_cur.next

        return new_head