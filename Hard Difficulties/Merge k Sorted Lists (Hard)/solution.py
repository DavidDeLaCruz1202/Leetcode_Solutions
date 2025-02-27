# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """

        # TODO: Thoughts for further optimization
        # --> Instead of searching through dict in O(N) time, create minheap with all of our values
        # Pop min from this minheap, try to find that value in dictionary
        # Keep popping while len(indexSet) of our value is 0
        # ---------------------------------------------------

        # Helper function to get minimum key from dictionary
        def findMin(inputDict):
            minVal = float('inf')
            for value in inputDict.keys():
                if value < minVal:
                    minVal = value

            return minVal

        # Create pseudo-head of list and reference to that head
        dummy = ListNode(0)
        curr = dummy

        # Dictionary to store values and the indices they can be found at
        vals = {}

        # Populate vals dictionary
        for index, node in enumerate(lists):
            value = node.val if node else float('inf')

            if vals.get(value) is None:
                vals[value] = set()
            vals[value].add(index)

        # Merge
        while True:
            # Get minimum
            minVal = findMin(vals)

            if minVal == float('inf'):
                break

            # Insert Node
            nextNode = ListNode(minVal)
            curr.next = nextNode
            curr = curr.next

            # Pop random index from dictionary value's set
            poppedIndex = vals[minVal].pop()

            # Delete key if set is empty
            if len(vals[minVal]) == 0:
                del vals[minVal]
            
            # Update node in node list
            lists[poppedIndex] = lists[poppedIndex].next if lists[poppedIndex] else None

            # Get value of our updated node
            val = lists[poppedIndex].val if lists[poppedIndex] else float('inf')

            # If updated node exists, add this node's index to the number we got from it
            if val != float('inf'):
                if vals.get(val) is None:
                    vals[val] = set()
                vals[val].add(poppedIndex)

        # Return next of our dummy node, which is head of our list
        return dummy.next




"""

---------- First solution (less optimized) ----------

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        
        #:type lists: List[Optional[ListNode]]
        #:rtype: Optional[ListNode]
        

        # Base Cases (empty input or all "None")
        if len(lists) == 0 or (len(set(lists)) == 1 and lists[0] == None):
            return

        # Create pseudo-head of list and reference to that head
        dummy = ListNode(0)
        curr = dummy

        # Gather initial values
        vals = []
        for node in lists:
            vals.append(node.val if node else float('inf'))

        # Iterate through both linked lists while a non-None type exists
        while True:
            minVal = min(vals)  # Get minimum value
            minIndex = vals.index(minVal)  # Get list index that had that value

            if minVal == float('inf'):
                break

            # Insert Node
            nextNode = ListNode(minVal)
            curr.next = nextNode
            curr = curr.next

            # Update the node in the list, and the value in the value list
            lists[minIndex] = lists[minIndex].next if lists[minIndex] else None
            vals[minIndex] = lists[minIndex].val if lists[minIndex] else float('inf')

            
        return dummy.next
"""