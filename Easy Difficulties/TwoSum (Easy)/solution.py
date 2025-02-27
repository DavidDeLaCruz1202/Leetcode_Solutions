class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen_elements = {}

        for index, num in enumerate(nums):
            # First check if dictionary has compliment element
            compliment = target - num
            if seen_elements.get(compliment) is not None:
                return [seen_elements.get(compliment), index]
            
            # If compliment isn't found, add key-val {number : index}
            seen_elements[num] = index