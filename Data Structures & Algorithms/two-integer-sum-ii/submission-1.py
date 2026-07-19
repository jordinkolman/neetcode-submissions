class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < len(numbers) - 1:
            print (l, r)
            print(numbers[l], numbers[r])
            while r > l:
                print(numbers[l], numbers[r])
                if numbers[l] + numbers[r] == target:
                    return [l+1,r+1]
                else:
                    r -= 1
            r = len(numbers) - 1
            l += 1
        return []