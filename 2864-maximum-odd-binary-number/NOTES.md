Better Leetcode solution. More simple. 

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        z = s.count('0')
        o = s.count('1')
        return '1'*(o-1)+'0'*z+'1'​
