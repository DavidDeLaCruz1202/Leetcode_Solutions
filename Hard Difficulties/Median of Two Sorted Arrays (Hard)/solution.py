class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        len_1 = len(nums1)
        len_2 = len(nums2)

        # ---- Base cases ----
        # Both inputs are length 0
        if len_1 == 0 and len_2 == 0:
            print("Invalid input!")
            return 0.0

        # nums2 has no elements
        elif len_2 == 0:
            # nums1 has 1 element
            if len_1 == 1:
                return nums1[0]

            # nums1 has 2 elements
            if len_1 == 2:
                return (float(nums1[0]) + float(nums1[1])) / 2.0

            # all other cases
            middle = (len_1 // 2) - 1
            if len_1 % 2 == 0:
                return (float(nums1[middle]) + float(nums1[middle + 1])) / 2.0
            else:
                return (nums1[middle + 1])

        # nums1 has no elements
        elif len_1 == 0:
            # nums2 has 1 element
            if len_2 == 1:
                return nums2[0]

            # nums2 has 2 elements
            if len_2 == 2:
                return (float(nums2[0]) + float(nums2[1])) / 2.0

            # all other cases
            middle = (len_2 // 2) - 1
            if len_2 % 2 == 0:
                return (float(nums2[middle]) + float(nums2[middle + 1])) / 2.0
            else:
                return (nums2[middle + 1])

        # Both lists have 1 element
        elif len_1 == 1 and len_2 == 1:
            return (float(nums1[0]) + float(nums2[0])) / 2.0
        # ---- End of base cases ----


        # Get combined lengths
        comb_len = len_1 + len_2

        # Set bool for if we need to find avg median or just median
        two_medians = comb_len % 2 == 0
        prev_median = 0  # For even length cases
        
        # Find the "middle" of the two combined lists
        middle = comb_len // 2  # Integer divison

        # List pointers
        iter_1, prev_iter_1 = 0, -1
        iter_2, prev_iter_2 = 0, -1

        # Getting initial element for comparison and incrementing
        if nums1[0] > nums2[0]:
            prev = nums2[0]
            iter_2 += 1
            prev_iter_2 += 1
        else:
            prev = nums1[0]
            iter_1 += 1
            prev_iter_1 += 1
        
        # Edge cases
        if iter_1 == len_1:
            prev_iter_1 = iter_1
        elif iter_2 == len_2:
            prev_iter_2 = iter_2

        # Iterate up until the middle index
        for i in range(1, middle + 1):

            # Cases where the end of one list is reached
            if prev_iter_1 == iter_1:
                prev = nums2[iter_2]

                if i + 2 == middle + 1 and two_medians:
                    prev_median = prev
                
                iter_2 += 1
                continue

            elif prev_iter_2 == iter_2:
                prev = nums1[iter_1]

                if i + 2 == middle + 1 and two_medians:
                    prev_median = prev
                
                iter_1 += 1
                continue

            
            # Other cases where we have not reached end of either list
            
            # Find the next closest element
            diff_1 = abs(nums1[iter_1] - prev)
            diff_2 = abs(nums2[iter_2] - prev)
            
            # Get element from nums2 since that's closer
            if diff_1 > diff_2:
                prev = nums2[iter_2]
                prev_iter_2 += 1
                if (iter_2 + 1) != len_2:
                    iter_2 += 1
                    
            # Otherwise, get element from nums1
            else:
                prev = nums1[iter_1]
                prev_iter_1 += 1
                if (iter_1 + 1) != len_1:
                    iter_1 += 1

            # Updating our variable for when we need two middle values
            if i + 2 == middle + 1 and two_medians:
                prev_median = prev

        # Final calculation
        if two_medians:
            return (float(prev) + float(prev_median)) / 2.0
        else:
            return prev