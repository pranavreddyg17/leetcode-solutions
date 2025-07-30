class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        hashset = set()
        longest = 0
        for r in range(n):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            w = (r-l) + 1
            longest = max(longest,w)
            hashset.add(s[r])
        return longest
        