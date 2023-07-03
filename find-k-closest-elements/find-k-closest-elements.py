class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        low, high = 0, n - 1
        while low <= high:
            mid = (low+high) >> 1
            if arr[mid] == x:
                start, end = mid - 1, mid + 1
                k -= 1
                break
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        
        if low > high:
            start = high
            end = low
            
        while k > 0:
            if start == -1:
                end+=1
            elif end == n:
                start-=1
            else:
                if abs(x-arr[start]) <= abs(arr[end] - x):
                    start-=1
                else:
                    end+=1
            k-=1
            
        return arr[start+1:end]