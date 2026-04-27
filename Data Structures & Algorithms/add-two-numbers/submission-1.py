# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num = 0
        place = 1
        current = l1
        while current:
            num = num + (current.val*place)
            place *= 10
            current = current.next
        num2 = 0
        place = 1
        current = l2
        while current:
            num2 = num2 + (current.val*place)
            place *= 10
            current = current.next
        total = num + num2
        dummy = ListNode(0)
        current = dummy
        if total == 0:
            return ListNode(0)
        while total > 0:
            digit = total % 10
            current.next = ListNode(digit)
            current = current.next
            total = total // 10
        head = dummy.next
        return head