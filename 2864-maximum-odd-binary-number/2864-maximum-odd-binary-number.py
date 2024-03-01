class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        t_one = 0
        t_zero = 0

        for i in s:
            if i == "1":
                t_one += 1
            else:
                t_zero += 1

        re_str = ""
        
        for i in range(t_one - 1):
            re_str += "1"

        for i in range(t_zero):
            re_str += "0"
        
        re_str += "1"
        return re_str
        