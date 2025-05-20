class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ans={}
        # for s in strs:
        #     sorteds = sorted(s)
        #     key = tuple(sorteds)
        #     if key not in ans:
        #         ans[key]=[s]
        #     else:
        #         ans[key].append(s)
        # return list(ans.values())
        res = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord("a")]+=1
            res[tuple(count)].append(s)
        return list(res.values())