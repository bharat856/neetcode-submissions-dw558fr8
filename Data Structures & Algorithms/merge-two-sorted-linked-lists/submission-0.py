# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        newHead = ListNode()
        temp1, temp2 = list1, list2
        if not list1:
            return list2

        if not list2:
            return list1

        if temp1.val <= temp2.val:
            newHead.val = temp1.val
            temp1 = temp1.next 
            newHead.next = self.mergeTwoLists(temp1, temp2)
        else:
            newHead.val = temp2.val
            temp2 = temp2.next
            newHead.next = self.mergeTwoLists(temp1, temp2)
            
        return newHead