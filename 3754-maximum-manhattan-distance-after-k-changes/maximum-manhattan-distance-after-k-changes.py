class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        return max(min(int(abs(xy.real)+abs(xy.imag))+k*2,i+1) 
            for i,xy in enumerate(accumulate(map({'N':1,'S':-1,'E':1j,'W':-1j}.get,s))))