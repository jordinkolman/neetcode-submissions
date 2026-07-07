class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        while left < len(nums) - 1:
            right = len(nums) - 1
            while right > left:
                if nums[left] + nums[right] == target:
                    return [left, right]
                right -= 1
            left += 1
        