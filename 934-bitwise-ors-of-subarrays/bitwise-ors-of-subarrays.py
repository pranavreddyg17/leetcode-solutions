class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        st = set()
        
        for i in range(len(arr)):
            num = arr[i]
            st.add(num)
            for j in range(i - 1, -1, -1):
                if (arr[j] | num) == arr[j]:
                    break
                arr[j] |= num
                st.add(arr[j])
        
        return len(st)