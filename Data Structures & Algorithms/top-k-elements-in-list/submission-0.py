class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1

        results = []
        for i in range(k):
            result = max(frequencies, key=frequencies.get)
            results.append(result)
            del frequencies[result]

        return results
