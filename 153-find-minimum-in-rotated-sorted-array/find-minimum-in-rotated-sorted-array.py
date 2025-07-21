class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        m = (l+r)//2
        curr_min = nums[-1]
        while l<=r:
            if nums[m]>curr_min:
                l = m+1
                m = (l+r)//2
            else:
                curr_min = nums[m]
                r = m-1
                m = (l+r)//2
        return curr_min
        