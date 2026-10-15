
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = ""
        lst1 = list(word1)
        lst2 = list(word2)

        for i in range(min(len(lst1), len(lst2))):
            word += lst1[i] + lst2[i]

        if len(lst1) > len(lst2):
            for i in range(len(lst2), len(lst1)):
                word += lst1[i]

        elif len(lst2) > len(lst1):
            for i in range(len(lst1), len(lst2)):
                word += lst2[i]

        return word
