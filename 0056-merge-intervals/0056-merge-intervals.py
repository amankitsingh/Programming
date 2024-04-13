### Answer 1 - using array
### TC- O(nlogn+n), SC - O(N)
### array is not sorted
'''
Intution 
sort the array
check the last element is less or greater, if last element in the list is less then append
else change the range
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])
        
        result = []
        for interval in intervals:
            # if result is empty then append in the result
            # if last element is less than new element then add to result
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                # if last element in the result is greateer or equal then the current the expand the range    
                result[-1][1] = max(interval[1], result[-1][1])
        return result
