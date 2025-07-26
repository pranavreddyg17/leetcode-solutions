class Solution:
    def maxArea(self, height: List[int]) -> int:
        # max_area = 0
        # n = len(height)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         area = min(height[i],height[j])*(j-i)
        #         max_area = max(max_area,area)
        # return max_area
        
        n = len(height)
        l = 0
        r = n-1
        max_area = 0
        while l<r:
            area = (r-l)* min(height[l],height[r])
            max_area = max(max_area,area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max_area
        
