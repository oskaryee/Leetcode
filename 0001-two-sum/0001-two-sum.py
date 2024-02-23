class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        for i in range(size):
            for j in range(i + 1, size):
                su = nums[i] + nums[j]
                if su == target:
                    return [i, j]
        return []        