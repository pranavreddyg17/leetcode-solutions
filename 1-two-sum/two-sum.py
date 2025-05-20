class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return (i,j)
        # return False
        
        # d = {}
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     if diff in d:
        #         return(d[diff],i)
        #     d[nums[i]]=i
        # return False

        d={}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in d:
                return(d[diff],i)
            d[n]=i
        return False
        