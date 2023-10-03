### Answer1 - top down approach, calculate the the value starting from bottom to up and cache them
### Time complexity - O(N*4*3), space complexity - O(N)

from typing import *
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp = [[-1 for j in range(4)] for i in range(n)]
    def findmax(day, last_index):
        if dp[day][last_index]!=-1:
            return dp[day][last_index]
        if day == 0:
            maxi = 0
            for i in range(3):
                if i!=last_index:
                    maxi = max(maxi, points[0][i])
            dp[day][last_index] = maxi
            return maxi
        maxi = 0
        for i in range(3):
            if i!=last_index:
                activity = points[day][i] + findmax(day-1, i)
                maxi = max(maxi, activity)
        dp[day][last_index] = maxi
        print(dp)
        return dp[day][last_index]
    
    return findmax(n-1,3)

### Answer 2 - bottom up approach, calculate the max in base case then go ahead.
### Time complexity - O(N*4*3), space complexity - O(N)

from typing import *

  
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp = [[0 for j in range(4)] for i in range(n)]
    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][2], points[0][0])
    dp[0][2] = max(points[0][1], points[0][0])
    dp[0][3] = max(points[0][1], points[0][2], points[0][0])
    
    for day in range(n):
        for last in range(4):
            dp[day][last] = 0
            for task in range(3):
                if task!=last:
                    activity = points[day][task] + dp[day-1][task]
                    dp[day][last] = max(activity, dp[day][last])
    return dp[n-1][3]

## Answer 3 - using space optimzation 1D array, take the prevarray and calculate the present
### Time complexity - O(N*4*3), space complexity - O(4)
from typing import *

  
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    prev = [0]*4
    prev[0] = max(points[0][1], points[0][2])
    prev[1] = max(points[0][0], points[0][2])
    prev[2] = max(points[0][1], points[0][0])
    prev[3] = max(points[0][1], points[0][2], points[0][0])

    for day in range(1, n):
        temp = [0]*4
        for last in range(4):
            temp[last] = 0
            for task in range(3):
                if task!= last:
                    activity = points[day][task] + prev[task]
                    temp[last] = max(temp[last], activity)
        prev = temp
    return prev[3]

### Answer 4
def ninjaTraining(n,points) -> int:
    a,b,c=points[0]
    for i in range(1,n):
       new_a=max(b,c)+points[i][0]
       new_b=max(a,c)+points[i][1]
       new_c=max(a,b)+points[i][2]
       a,b,c=new_a,new_b,new_c
    return max(a,b,c)
