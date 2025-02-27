# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummyHead = ListNode(0)
        curr = dummyHead
        # id(dummyHead) == id(curr) is True

        carry = 0

        # While we don't have more to add
        while l1 != None or l2 != None or carry != 0:
            # Get node values if they exist, otherwise default them to 0
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0

            # Calculate current sum and its carry
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10

            # Create new node and update pointers
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode  # Same as curr = curr.next

            # Update node pointers to next if they exist, otherwise default to None
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return dummy head's next, which is the start of our head
        return dummyHead.next
    



# Personal code for testing
if __name__ == '__main__':
    nums1 = [2, 4, 3]
    nums2 = [5, 6, 4]

    l1 = ListNode(nums1[0])
    l2 = ListNode(nums2[0])

    temp1 = l1
    temp2 = l2

    for i in range(1, 3):
        temp1.next = ListNode(nums1[i])
        temp2.next = ListNode(nums2[i])

        temp1 = temp1.next
        temp2 = temp2.next

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    while result != None:
        print(result.val, end=" ")
        result = result.next