class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checked = []
        for _, num in enumerate(nums):
            if num in checked:
                return True
            else:
                checked.append(num)
        
        return False