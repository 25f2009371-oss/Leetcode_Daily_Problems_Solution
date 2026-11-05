class Solution:
    def minMoves(self, nums: List[int]) -> int:
        large=max(nums)
        count=0
        length=len(nums)

        for i in range(length):
            while nums[i]!=large:
                nums[i]+=1
                count+=1
        return count