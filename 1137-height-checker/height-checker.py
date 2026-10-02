class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        s=sorted(heights)
        count=0
        for i in range(len(heights)):
            for j in range(len(s)):
                if i==j:
                    if heights[i]!=s[j]:
                        count+=1
        return count