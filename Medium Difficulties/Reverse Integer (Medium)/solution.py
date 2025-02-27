class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        # Convert int to string
        str_x = str(x)

        # Negative case
        if str_x[0] == '-':
            retStr = "-"
            retStr += str_x[-1:0:-1]  # Iterate from last number to first number (exclusive)
        
        # Positive case
        else:
            retStr = str_x[::-1]  # Just return reverse of number

        # Check for invalid reverse output
        upperRange, lowerRange = pow(2, 31) - 1, -pow(2, 31)
        if(not(lowerRange <= int(retStr) <= upperRange)):
            return 0

        return int(retStr)