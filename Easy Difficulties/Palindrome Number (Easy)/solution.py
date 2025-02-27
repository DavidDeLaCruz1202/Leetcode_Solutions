class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        # Easy solution (good speed)
        # --> Only convert string once instead of doing str(x) == str(x)[::-1] which converts twice
        str_x = str(x)
        return(str_x == str_x[::-1])

        # Not using conversions
        """
        original = x
        total = 0

        while original > 0:
            total += original % 10
            original //= 10
            if original > 0:
                total *= 10

        return total == x
        """