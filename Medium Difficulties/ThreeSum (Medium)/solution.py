class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        target = 0
        length = len(nums)
        triplets = [] 
        seen_numbers = {}  # Dictionary
        zero_tripletable = True
        
        # Edge case for three zeros
        if len(nums) == 3 and nums[0] == nums[1] == nums[2] == 0:
            return [[0,0,0]]

        # Populate a dictionary (hashmap) with values we've found and where
        for i, num in enumerate(nums):
            if seen_numbers.get(num) is not None:
                seen_numbers[num].append(i)
            else:
                seen_numbers[num] = [i]

        # Go through the list and find the triplets
        for i in range(length - 1):
            firstAdd = nums[i]
            for j in range(i + 1, length):
                # Set variables for our first two numbers
                secondAdd = nums[j]

                # Get compliment and its indices in the list (if they exist)
                compliment = target - secondAdd - firstAdd
                compliment_indices = seen_numbers.get(compliment)

                if compliment_indices is None:
                    continue

                for index in compliment_indices:
                    # Ensure unique indices
                    if index != i and index != j:
                        duplicate = False

                        # Base case of empty triplets
                        if len(triplets) == 0:
                            triplets.append((firstAdd, secondAdd, compliment))
                            if firstAdd == 0 and secondAdd == 0 and compliment == 0:
                                zero_tripletable = False
                            break
                        
                        # Edge case for triplet of all zeros
                        if zero_tripletable and firstAdd == 0 and secondAdd == 0 and compliment == 0:
                            triplets.append((firstAdd, secondAdd, compliment))
                            zero_tripletable = False
                            break
                        
                        # Ensure unique triplet
                        for triplet in triplets:
                            duplicate = (firstAdd in triplet) and (secondAdd in triplet) and (compliment in triplet)
                            if duplicate:
                                break

                        if not duplicate:
                            triplets.append((firstAdd, secondAdd, compliment))
                        
        return triplets
    



    """
    
    >> BETTER SOLUTION! <<
    
        nums.sort()
        n = len(nums)

        # Hash tables
        solutions = set()
        unique_set = set(nums)  # Remove duplicates from nums

        # All zero edge cases
        if len(unique_set) == 1 and 0 in unique_set and len(nums) > 2:
            return [[0, 0, 0]]

        # Go from left to right
        i = 0
        while i < n - 2:

            # Our three numbers
            num = nums[i]  # Initialiiy first variable
            left = i + 1   # Initially second veriable
            right = n - 1  # Initially last variable

            # Iterate while the left is less than the right
            while left < right:
                left_num = nums[left]
                right_num = nums[right]

                # Check if sum is 0
                s = num + left_num + right_num 
                if s == 0:
                    solutions.add(tuple([right_num, num, left_num]))  # Set automatically denies duplicates
                    right -= 1
                    left += 1

                # If sum is too big, decrement larger variable (right)
                elif s > 0:
                    right -= 1

                # If sum is too small, increment smaller variable (left)
                else:
                    left += 1

            # Increment left-most variable
            i += 1

        # Return solutions as a list
        return list(solutions)
    
    """