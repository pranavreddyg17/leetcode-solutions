from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        length = 0
        center_used = False

        for word in list(count):  # Iterate over a copy of the keys
            rev = word[::-1]
            if word != rev:
                pairs = min(count[word], count.get(rev, 0))
                length += pairs * 4
                count[word] -= pairs
                count[rev] -= pairs
            else:
                pairs = count[word] // 2
                length += pairs * 4
                count[word] -= pairs * 2
                if count[word] > 0 and not center_used:
                    length += 2
                    center_used = True

        return length
