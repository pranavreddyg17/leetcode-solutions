class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Doesn't satisfy unicode
        if len(s) != len(t):
            return False
        n = len(s)
        counts = [0]*26
        for c in s:
            counts[ord(c)-ord("a")] += 1
        countt = [0]*26
        for c in t:
            countt[ord(c)-ord("a")] += 1
        if counts == countt:
            return True
        else: 
            return False