# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        hashMap = {}
        temp = head
        i = 0
        while temp:
            hashMap[i] = temp
            i += 1
            temp = temp.next
        right = i - 1
        left = 0
        while left < right:
            hashMap[left].next = hashMap[right]
            left += 1
            if left == right:
                break
            hashMap[right].next = hashMap[left]
            right -= 1
        hashMap[left].next = None
            