class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += ("" + str(len(s)) + "#" + s)

        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        curr = 0
        while curr < len(s):
            numString = ""
            while s[curr] != "#":
                numString += s[curr]
                print(numString)
                curr += 1
            try:
                strLen = int(numString)
            except ValueError:
                print("error parsing string length")
                return [""]
            
            curr += 1
            word = ""
            for _ in range(strLen):
                word += s[curr]
                curr += 1

            res.append(word)

        return res