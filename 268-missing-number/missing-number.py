class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        lst=[]
        for i in range(len(nums)+1):
            lst.append(i)
        


        for i in lst:
            if i not in nums:
                return i