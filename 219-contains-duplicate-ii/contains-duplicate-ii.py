class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for key,value in enumerate(nums):
            if value in d and abs(key- d[value]) <=k:
                return True
            d[value] = key
        return False