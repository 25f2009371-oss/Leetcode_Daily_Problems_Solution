class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum=0
        y=x
        while y>0:
            sum+=y%10
            y=y//10
        if(x%sum==0):
            return sum
        else:
            return -1

        