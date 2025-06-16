class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        my_list = []
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                my_list.append(nums[j]-nums[i])

        max_val = max(my_list)

        if max_val <= 0:
            return -1
        else:
            return max_val