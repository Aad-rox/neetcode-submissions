# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        currentNode = head
        prevNode = None
        nextNode = None
        if currentNode is not None:
            while (currentNode.next):
                nextNode = currentNode.next
                currentNode.next = prevNode
                prevNode = currentNode
                currentNode = nextNode
        if currentNode is not None:
            currentNode.next = prevNode
        
        return currentNode
           



            
            
        