class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        left, right = 0, 0
        while right < len(s):
            while s[right] != "#":
                # increment right pointer until end of length num is reached
                right += 1
            # set length as substring between left and right
            length = int(s[left:right])
            # move pointers to start of word
            left = right + 1
            right = left

            # add string to result list
            res.append(s[left:right+length])

            # move pointers to start of next tring
            left = right + length
            right = left

        return res