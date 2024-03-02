class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        r_p = -1
        min, max = -1, len(nums)
        
        for i in range(max):
            if nums[i] >= 0:
                r_p = i
                break
        else:
            r_p = max
            
        l_p = r_p - 1

        final = []
        # Find the middle point and expand left/right until you reach an end
        while l_p > min and r_p < max:
            l = nums[l_p] * nums[l_p]
            r = nums[r_p] * nums[r_p]

            if l <= r:
                final.append(l)
                l_p -= 1
            if l >= r:
                final.append(r)
                r_p += 1

        # If we reach the max end we fill the rest of the negative numbers
        while l_p > min:
            l = nums[l_p] * nums[l_p]
            final.append(l)
            l_p -= 1
        
        # If we reach the min end we fill the rest of the positive numbers
        while r_p < max:
            r = nums[r_p] * nums[r_p]
            final.append(r)
            r_p += 1

        return final