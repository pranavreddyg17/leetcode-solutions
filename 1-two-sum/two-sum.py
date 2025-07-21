class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for k,v in enumerate(nums):
            diff = target - v
            if diff in d:
                return [d[diff],k]
            else:
                d[v] = k