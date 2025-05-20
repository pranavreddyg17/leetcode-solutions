from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        delta = [0] * (n + 1)  # difference array
        
        # Step 1: Build difference array for all queries
        for l, r in queries:
            delta[l] += 1
            if r + 1 < n:
                delta[r + 1] -= 1

        # Step 2: Apply prefix sum to calculate how many times each index should be decremented
        dec = 0
        for i in range(n):
            dec += delta[i]
            nums[i] = max(0, nums[i] - dec)  # decrement but don't go below 0

        # Step 3: Check if array is all zeros
        return all(num == 0 for num in nums)
