# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        hashMap = {}
        temp = head
        i = 1
        while temp:
            hashMap[i] = temp
            i += 1
            temp = temp.next
        j = i - n 
        if hashMap[j] == head:
            return head.next
        else:
            hashMap[j - 1].next = hashMap[j].next
            return head
        