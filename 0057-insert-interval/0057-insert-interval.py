### Answer - similar to https://github.com/amankitsingh/Programming/tree/master/0056-merge-intervals
### TC - O(NlogN+N), SC - O(N)
'''
Intution:
append the new interval to the intervals list and sort the array based on the first element
then check if the last element is greater or less the the result element and expand the array list accordingly 
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        
        result = []
        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(interval[1], result[-1][1])
        return result
