class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # dic={}
        # for n in nums:
        #     if n in dic:
        #         return True
        #     else:
        #         dic[n] = n
        # return False


        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
            
        # brute force
        # for i in range(len(nums)):
        #     for j in range(i+1,(len(nums))):
        #         if nums[i]==nums[j]:
        #             return True
        # return False

        # sorted solution
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i]==nums[i+1]:
        #         return True
        # return False
