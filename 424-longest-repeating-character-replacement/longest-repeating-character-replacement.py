class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        counts = [0]*26
        l = 0
        for r in range(len(s)):
            counts[ord(s[r])-65] += 1
            if (r-l+1) - max(counts) >k:
                counts[ord(s[l])-65] -= 1
                l += 1
            w = r-l+1
            longest = max(longest,w)
        return longest
        