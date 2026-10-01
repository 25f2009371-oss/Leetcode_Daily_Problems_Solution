def is_prime(n):
    if n <= 1:
        return False    
    if n == 2:
        return True
    if n % 2 == 0:
        return False        
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False  # Found a factor, not prime
            
    return True  # No factors found, it's prime


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        result=0

        for i in range(left,right+1):
            b=bin(i)[2:]
            count=0
            b=str(b)
            for i in b:
                if i=='1':
                    count+=1
            
            #prime function
            if is_prime(count):
                result+=1



        return result
        