class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        lst=[]
        for i in range(n):
            lst.append(start+2*i)
        try:
            result=0
            for i in range(len(lst)):
                result ^= lst[i]
            return result

        except IndexError:
            return 0        