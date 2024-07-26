### Answer - similar to https://github.com/captain-indo/Programming/tree/master/0056-merge-intervals - in this the array was not sorted 
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


### Answer 2 - after observation
### TC - O(N), SC - O(N)
'''
Intution
we observed that there are 3 case
1. when there is no overlap
2. when there is overlap, at that we need to take min of interval and new interval for start and max for end
3. when there is no overlap
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        result = []
        
        #case 1: when no overlap
        while i<n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i+=1
        
        #case 2: when overlap
        while i<n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i+=1
        result.append(newInterval)
    
        
        #case 3: when overlaps are merged
        while i<n:
            result.append(intervals[i])
            i+=1
        return result
