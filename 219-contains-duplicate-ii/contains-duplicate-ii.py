class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for key, value in enumerate(nums):
            if value in d and (key - d[value])<=k:
                return True
            else:
                d[value]= key
        return False