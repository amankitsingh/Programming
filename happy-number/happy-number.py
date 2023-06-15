class Solution:
    def isHappy(self, n: int) -> bool:
        
        def next_number(n):
            total_sum = 0
            while n > 0 :
                n,digit = divmod(n, 10)
                total_sum+=digit**2
            return total_sum
        
        seen = set()
        
        while n!=0 and n not in seen:
            seen.add(n)
            n= next_number(n)
        
        return n==1
            