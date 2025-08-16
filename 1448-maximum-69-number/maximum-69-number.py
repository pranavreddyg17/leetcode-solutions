class Solution:
    def maximum69Number (self, num: int) -> int:
        s = list(str(num))   # convert to list so we can modify
        for i in range(len(s)):
            if s[i] == '6':
                s[i] = '9'   # assign correctly
                break
        return int("".join(s))  # convert back to int
