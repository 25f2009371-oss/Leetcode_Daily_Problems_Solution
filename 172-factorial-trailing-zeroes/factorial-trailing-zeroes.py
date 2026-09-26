class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        r = 1
        for i in range(1, n + 1):
            r *= i
        count = 0
        
        if r % 10 != 0:
            return 0
        while r % 10 == 0:
            count += 1
            r = r // 10
        return count