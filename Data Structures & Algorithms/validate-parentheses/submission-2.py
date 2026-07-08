class Solution:
    def isValid(self, s: str) -> bool:
        toPair = []
        for char in s:
            if char in '[{(':
                toPair.append(char)
                continue
            try:
                comp = toPair.pop()
            except IndexError:
                return False
            match char:
                case ']':
                    if comp != '[':
                        return False
                case '}':
                    if comp != '{':
                        return False
                case ')':
                    if comp != '(':
                        return False
                case _:
                    continue
        if len(toPair) > 0:
            return False
        return True                    
