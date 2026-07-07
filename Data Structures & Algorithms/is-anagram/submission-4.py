class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_frequency = {}
        for char in s:
            if char in char_frequency:
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1
        for char in t:
            if char in char_frequency:
                char_frequency[char] -= 1
            else:
                return False
        
        for char in char_frequency:
            if char_frequency[char] < 0 or char_frequency[char] > 0:
                return False
        return True