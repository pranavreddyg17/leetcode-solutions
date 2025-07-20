class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        prev = nums[0]
        for i in nums:
            if count == 0:
                prev = i
                count +=1
            elif prev == i:
                count +=1
            else:
                count -=1
        return prev

        