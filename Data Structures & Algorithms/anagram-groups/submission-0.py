class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a dict for storing the tuple of frequency as key, with list of strings asvalues
        result = defaultdict(list)
        for s in strs:
            # initiate character frequency array
            count = [0]*26
            for c in s:
                # increment the correct location in the frequency array based on character
                count[ord(c) - ord('a')] += 1
            # append the string to the frequency array key in hashmap
            result[tuple(count)].append(s)
        # return list of grouped anagrams by frequency array
        return list(result.values())
        