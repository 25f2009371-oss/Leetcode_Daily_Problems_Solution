class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        lst=[]

        for i in nums:
            lst.append(i)
        for i in nums:
            lst.append(i)
        return lst