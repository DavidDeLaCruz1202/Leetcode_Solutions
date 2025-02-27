class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        # Dict to store numbers and easily check for duplicates
        rowNums = {}
        colNums =  {0 : {}, 
                    1 : {}, 
                    2 : {}, 
                    3 : {}, 
                    4 : {}, 
                    5 : {}, 
                    6 : {}, 
                    7 : {}, 
                    8 : {}}  # 9 dicts for columns
        subBox1Nums = {}
        subBox2Nums = {}
        subBox3Nums = {}

        # Loop through rows
        for row in range(9):
            # Reset sub-boxes every 3 rows
            if row % 3 == 0:
                subBox1Nums = {}
                subBox2Nums = {}
                subBox3Nums = {}

            # Reset row dictionary every row
            rowNums = {}

            # Loop through columns
            for col in range(9):
                currNum = board[row][col]

                # Only check cells that are valid
                if currNum != '.':

                    # Checking for row duplicates
                    if rowNums.get(currNum) is not None:
                        return False  # Duplicate row number found, so return False
                    rowNums[currNum] = True

                    # Checking for sub-box duplicates
                    if col < 3:
                        if subBox1Nums.get(currNum) is not None:
                            return False  # Duplicate sub-box number found
                        subBox1Nums[currNum] = True

                    elif col < 6:
                        if subBox2Nums.get(currNum) is not None:
                            return False  # Duplicate sub-box number found
                        subBox2Nums[currNum] = True

                    else:
                        if subBox3Nums.get(currNum) is not None:
                            return False  # Duplicate sub-box number found
                        subBox3Nums[currNum] = True

                    # Checking for column duplicates
                    if colNums[col].get(currNum) is not None:
                        return False  # Duplicate column number found, so return False
                    colNums[col][currNum] = True
        
        return True