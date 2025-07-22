class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = [0]*26
        for c in s:
            counts[ord(c)-ord("a")] += 1
        countt = [0]*26
        for c in t:
            countt[ord(c)-ord("a")] += 1
        if counts == countt:
            return True
        return False
