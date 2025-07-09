class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = [startTime[0]] + [startTime[i] - endTime[i-1] for i in range(1, n)] + [eventTime - endTime[-1]]
        size = min(k + 1, len(gaps))
        curr = sum(gaps[:size])
        best = curr
        for i in range(size, len(gaps)):
            curr += gaps[i] - gaps[i - size]
            if curr > best:
                best = curr
        return best