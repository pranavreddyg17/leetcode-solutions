class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
            
        scount,tcount = {},{}
        for i in range(len(s)):
            scount[s[i]]=scount.get(s[i],0)+1
            tcount[t[i]]=tcount.get(t[i],0)+1
        for c in scount:
            if scount[c]!=tcount.get(c,0):
                return False
        return True

        # doesnt satsify unicode
        # counts=[0]*26
        # for c in s:
        #     counts[ord(c)-ord("a")]+=1
        # countt=[0]*26
        # for c in t:
        #     countt[ord(c)-ord("a")]+=1
        # if counts==countt:
        #     return True
        # return False

        #return Counter(s) == Counter(t)

        #return sorted(s) == sorted(t)
