# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        # Create pseudo-head of list and reference to that head
        dummy = ListNode(0)
        curr = dummy

        # Iterate through both linked lists
        while list1 != None or list2 != None:

            # Values = node value if it exists, otherwise it equals None
            val1 = list1.val if list1 else None
            val2 = list2.val if list2 else None

            # Append node to linked list with value 1
            if val2 == None or (val1 <= val2 and val1 != None):
                nextNode = ListNode(val1)
                curr.next = nextNode
                curr = curr.next
                list1 = list1.next if list1 else None
            
            # Append node to linked list with value 2
            else:
                nextNode = ListNode(val2)
                curr.next = nextNode
                curr = curr.next
                list2 = list2.next if list2 else None
            
        return dummy.next