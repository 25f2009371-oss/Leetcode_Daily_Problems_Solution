class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        a_b=str(bin(a))
        b_b=str(bin(b))
        c_a=0
        c_b=0
        for i in a_b:
            if i=="1":
                c_a+=1
        for i in b_b:
            if i=="1":
                c_b+=1
        
        if c_a>=c_b:
            return c_a*c_b
        else:
            return int(c_b/c_a)
        
        