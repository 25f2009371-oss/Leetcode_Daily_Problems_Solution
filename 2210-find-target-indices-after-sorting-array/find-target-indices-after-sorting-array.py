class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        rslt=[]
        for i in range(len(nums)):
            if nums[i]==target:
                rslt.append(i)
        return rslt