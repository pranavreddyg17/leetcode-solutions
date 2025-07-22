class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target :
                return m
            
            # search in left part of the sorted array
            if nums[l]<=nums[m]:
                if target>nums[m] or target<nums[l]:
                    l = m+1
                else:
                    r = m-1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m-1
                else:
                    l = m+1
        return -1


