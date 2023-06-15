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
    
    
'''
Intuition

The previous two approaches are the ones you'd be expected to come up with in an interview. This third approach is not something you'd write in an interview, but is aimed at the mathematically curious among you as it's quite interesting.

What's the biggest number that could have a next value bigger than itself? Well we know it has to be less than 243243243, from the analysis we did previously. Therefore, we know that any cycles must contain numbers smaller than 243243243, as anything bigger could not be cycled back to. With such small numbers, it's not difficult to write a brute force program that finds all the cycles.

If you do this, you'll find there's only one cycle: 4→16→37→58→89→145→42→20→4. All other numbers are on chains that lead into this cycle, or on chains that lead into 111.

Therefore, we can just hardcode a HashSet containing these numbers, and if we ever reach one of them, then we know we're in the cycle. There's no need to keep track of where we've been previously.

'''
# Answer 2
def isHappy(self, n: int) -> bool:

    cycle_members = {4, 16, 37, 58, 89, 145, 42, 20}

    def get_next(number):
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit ** 2
        return total_sum

    while n != 1 and n not in cycle_members:
        n = get_next(n)

    return n == 1
            
'''
An alternative approach would be to recognise that all numbers will either end at 1, or go past 4 (a member of the cycle) at some point. 
Therefore, instead of hardcoding the entire cycle, we can just hardcode the 4.
'''
#Answer 3
class Solution:
    
    def isHappy(self, n: int) -> bool:
        
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum
        
        while n != 1 and n != 4:
            n = get_next(n)
            
        return n == 1
