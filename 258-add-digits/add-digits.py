class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            st=0
            while num>0:
                st+=num%10
                num=num//10
            num=st
        return num

        