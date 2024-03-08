class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        d = {}
        max = 1

        for i in nums:
            if i in d:
                d[i] += 1
                if d[i] > max:
                    max = d[i]
            else:
                d[i] = 1
        
        total = 0
        if max > 1:
            for k,v in d.items():
                if v == max:
                    total += max
            return total
        else:
            return len(set(nums))