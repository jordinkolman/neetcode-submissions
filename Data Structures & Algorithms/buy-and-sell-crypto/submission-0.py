class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        left = 0
        right = len(prices) - 1

        while left < right:
            while left < right:
                profit = prices[right] - prices[left]
                if profit > max:
                    max = profit
                right -= 1
            right = len(prices) - 1
            left += 1
        
        return max