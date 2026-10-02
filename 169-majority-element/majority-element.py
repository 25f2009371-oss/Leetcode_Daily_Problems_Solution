class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        dct={}
        for i in nums:
            if i not in dct:
                dct[i]=1
            else:
                dct[i]+=1
        
        for i in dct:
            if dct[i]>len(nums)/2:
                return i       