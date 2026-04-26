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
        if head is None:
            return None
        '''
        Create a new head with the  
        '''
        hashMap = {}
        temp = head
        while temp:
            hashMap[temp] = Node(temp.val)
            temp = temp.next
        temp = head
        while temp:
            if temp.next:
                hashMap[temp].next = hashMap[temp.next]
            else:
                hashMap[temp].next = None
            if temp.random:
                hashMap[temp].random = hashMap[temp.random]
            else:
                hashMap[temp].random = None
            temp = temp.next
        return hashMap[head]