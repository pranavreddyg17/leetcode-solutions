class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        nums=[]
        for i in range(len(words)):
            if x in list(words[i]):
                nums.append(i)
        return nums

        