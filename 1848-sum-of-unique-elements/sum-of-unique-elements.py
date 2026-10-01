class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        dct={}
        for i in nums:
            if i not in dct:
                dct[i]=1
            else:
                dct[i]+=1
        st=0
        for i in dct:
            if dct[i]==1:
                st+=i
        return st


        