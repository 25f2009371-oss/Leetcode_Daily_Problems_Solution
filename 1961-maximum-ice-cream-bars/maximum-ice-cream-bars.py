class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        sum=0
        count=0
        for i in costs:
            sum+=i
            if(sum<=coins):
                count+=1
            if sum>coins:
                break

        return count
        