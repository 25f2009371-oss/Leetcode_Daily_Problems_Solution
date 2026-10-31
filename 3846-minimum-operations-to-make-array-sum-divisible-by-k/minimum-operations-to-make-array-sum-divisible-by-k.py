class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count=0
        sum=0
        for i in nums:
            sum+=i

        if sum%k==0:
            return count

        elif sum%k>0:
            count=sum%k
        
        return count