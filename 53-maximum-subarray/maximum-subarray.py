class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Kadane's algorithm
        n = len(nums)
        currSum = 0
        maxSum = float('-inf')
        for n in nums:
            currSum += n
            maxSum = max(maxSum,currSum)
            if currSum<0:
                currSum = 0
        return maxSum
