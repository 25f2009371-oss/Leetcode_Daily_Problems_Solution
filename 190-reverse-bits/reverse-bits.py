class Solution:
    def reverseBits(self, n: int) -> int:
        x=bin(n)[2:]
        x=x.zfill(32)
        x=x[::-1]
        return int(x,2)

        