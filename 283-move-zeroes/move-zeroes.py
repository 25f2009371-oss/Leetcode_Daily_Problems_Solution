class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=0
        for i in nums[:]:
            if i==0:
                nums.remove(i)
                count+=1
        
        while(count!=0):
            count-=1
            nums.append(0)