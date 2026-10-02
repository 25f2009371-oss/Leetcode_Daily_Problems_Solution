class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dct={}
        for i in nums:
            if i not in dct:
                dct[i]=1
            else:
                dct[i]+=1
            
        for i in dct:
            if dct[i]>1:
                return True
        return False
        