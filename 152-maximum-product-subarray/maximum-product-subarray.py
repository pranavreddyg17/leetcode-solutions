class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')
        maxCurr = 1
        minCurr = 1
        for n in nums:
            if n == 0:
                res = max(res,0)
                minCurr = 1
                maxCurr = 1
                continue
            temp = maxCurr
            maxCurr = max(maxCurr*n,minCurr*n,n)
            minCurr = min(temp*n,minCurr*n,n)
            res = max(res,maxCurr)
        return res