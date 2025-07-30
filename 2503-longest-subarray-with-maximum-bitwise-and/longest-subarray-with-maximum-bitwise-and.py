class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = count = 0
        maxVal = max(nums)
        for num in nums:
            count = count + 1 if num == maxVal else 0
            res = max(res, count)
        return res     