
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        cnt = 0
        prev_prev = prev = nums[0]
        for num in nums:
            if prev != num:
                if prev_prev > prev < num or prev_prev < prev > num:
                    cnt += 1
                prev_prev, prev = prev, num
        return cnt  