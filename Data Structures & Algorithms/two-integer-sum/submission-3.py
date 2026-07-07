class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {num:nums.index(num) for num in nums}
        for i in range(len(nums)):
            complement = target - nums[i] 
            if complement in vals and vals[complement] != i:
                return sorted([i, vals[complement]])