class Solution:
 def twoSum(self, nums: List[int], target: int) -> List[int]:
    d = {}
    n = len(nums)
    for i in range(n) :
        diff = target - nums[i]
        if diff in d:
            return [d[diff],i]
        d[nums[i]] = i
    return False
    # Naive approach uses 2 for loops, you can also use 2 pointers.
   # d = {}
   # for k,v in enumerate(nums):
   #     diff = target - v
   #     if diff in d:
   #         return [d[diff],k]
   #     else:
   #         d[v] = k
