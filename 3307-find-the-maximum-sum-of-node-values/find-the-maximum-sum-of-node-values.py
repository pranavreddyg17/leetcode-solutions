class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        ans = total = sum(nums)
        diffs = [(nums[i] ^ k) - nums[i] for i in range(len(nums))]
        diffs.sort(reverse=True)

        for i in range(0, len(nums), 2):
            if i + 1 < len(nums):
                total += (diffs[i] + diffs[i + 1])
                ans = max(ans, total)
        
        return ans    