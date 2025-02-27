class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Sort Numbers
        nums.sort()

        # Base cases
        # if only one element or if the list has elements that are all negatives or zeros
        if len(nums) == 1 or nums[-1] <= 0:
            # If first element equal to or less than zero, return 1
            if nums[0] <= 0:
                return 1
            
            # For all other cases, return 1 if the first element isn't one, otherwise return first element + 1
            else:
                return 1 if nums[0] != 1 else nums[0] + 1

        # Remove numbers that are too large
        while nums[-1] >= 2**30:
            nums.remove(nums[-1])

        # Remove any negatives or zeros
        while nums[0] <= 0:
            nums.remove(nums[0])

        # Store last element and upper limit of list before set conversion
        upperLimit = nums[-1]
        lastNum = nums[-1]

        # Convert nums list to set, and store its current length
        nums = set(nums)
        numsLen = len(nums)

        for x in range(1, upperLimit):
            # Try to discard our current integer
            nums.discard(x)

            # If the lengths are the same, that means the number wasn't found
            if len(nums) == numsLen:
                return x  # So return x

            # Update numsLen when the number was found
            numsLen = len(nums)

        # When we've gone through the entire range and didn't find the number, that means we're missing the last number + 1
        return lastNum + 1