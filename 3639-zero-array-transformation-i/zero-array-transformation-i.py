class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        delta = [0]*(n+1)
        for l,r in queries:
            delta[l] += 1
            if delta[r]<=n:
                delta[r+1] -=1
        cop=0
        for i in range(len(nums)):
            cop+=delta[i]
            if cop<nums[i]:
                return False
        return True

