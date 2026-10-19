class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        res1=""
        res2=""

        for i in word1:
            for j in i:
                res1+=j

        for i in word2:
            for j in i:
                res2+=j

        return res1==res2

        