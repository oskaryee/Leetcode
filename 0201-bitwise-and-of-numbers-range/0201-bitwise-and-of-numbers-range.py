class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """ 
        code takes too long. Need shift operators instead of iterating through all the numbers. 
        
        total = left
        min = left + 1
        max = right + 1

        for i in range(min, max):

            if total == 0:
                return 0
            
            total &= i


        return total
        """
        
        count = 0
        while left != right :
            left >>= 1
            right >>= 1
            count += 1

        return (left << count)

