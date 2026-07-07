class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for i, num in enumerate(nums):
            complement = target - num 
            if complement in vals:
                return [vals[complement], i]
            vals[num] = i