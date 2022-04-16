# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp:
            length+=1
            temp = temp.next
            
        if length==1:
            return
        
        mid = length//2 
        
        count = 0
        temp = head
        while temp:
            if count==mid-1:
                temp.next = temp.next.next
                break
            else:
                count+=1
                temp = temp.next
                
                
        return head
