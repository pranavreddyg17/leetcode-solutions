class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        
        n = len(baskets)

        seg = [float("-inf")]*(4*n)

        def build_tree(l, r, pos, idx):
            
            if l > r:
                return

            if l == r:
                seg[pos] = baskets[idx]
                return
            

            mid = l + (r-l)//2

            if idx <= mid:
                build_tree(l, mid, 2*pos + 1, idx)
            else:
                build_tree(mid+1, r, 2*pos + 2, idx)

            seg[pos] = max(seg[2*pos + 1], seg[2*pos + 2])

        ans = 0

        def check_update_basket(val, pos, l, r):
            nonlocal ans

            if l > r:
                return
            
            if seg[pos] < val:
                return

            if l == r:
                seg[pos] = float("-inf")
                ans += 1
                return 
            
            
            mid = l + (r-l)//2

            if seg[2*pos + 1] >= val:
                check_update_basket(val, 2*pos+1, l , mid)
            else:
                check_update_basket(val, 2*pos + 2, mid + 1, r)
            
            seg[pos] = max(seg[2*pos+1], seg[2*pos+2])

        for i in range(n):
            _ = build_tree(0, n-1, 0, i)
        
        for i in range(len(fruits)):
            check_update_basket(fruits[i], 0, 0, n-1)

        return len(fruits) - ans
