class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')
        minCurr = 1
        maxCurr = 1
        for n in nums:
            temp = maxCurr
            maxCurr = max(maxCurr*n,minCurr*n,n)
            minCurr = min(temp*n,minCurr*n,n)
            res = max(res,maxCurr)
        return res