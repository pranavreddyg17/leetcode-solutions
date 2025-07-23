class Solution:
    def climbStairs(self, n: int) -> int:
        # memo = {1:1,2:2}
        # def climb(n):
        #     if n in memo:
        #         return memo[n]
        #     else:
        #         memo[n] = climb(n-1) +climb(n-2)
        #         return memo[n]
        # return climb(n)
        if n==1:
            return 1
        if n==2:
            return 2
        first = 1
        second = 2
        for i in range(3,n+1):
            curr_sum = first + second
            first = second
            second = curr_sum
        return second