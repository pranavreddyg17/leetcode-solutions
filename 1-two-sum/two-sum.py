class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        n = len(nums)
        for i in range(n):
            diff = target - nums[i]
            if diff in d:
                return [d[diff],i]
            else:
                d[nums[i]] = i
        