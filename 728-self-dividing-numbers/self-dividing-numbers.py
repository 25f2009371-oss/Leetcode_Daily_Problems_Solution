class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        result=[]
        for i in range(left,right+1):
            digit=i
            l=len(str(i))
            count=0
            lst=[]
            while digit>0:
                lst.append(digit%10)
                digit=digit//10
            
            for k in lst:
                if k>0:
                    if i%k==0:
                        count+=1

            if count==l:
                result.append(i)
        return result
                 
            
        