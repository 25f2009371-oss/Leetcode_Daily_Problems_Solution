class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        rslt=[]
        m=max(candies)
        for i in candies:
            if i+extraCandies>=m:
                rslt.append(True)
            else:
                rslt.append(False)
                
        return rslt
        