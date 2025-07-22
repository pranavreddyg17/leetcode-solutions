class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = [1]*n
        p = nums[n-1]
        for i in range(1,n):
            l[i] = l[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            l[i] = l[i]*p
            p = p*nums[i]
            print(p)
            print(l[i])
        return l