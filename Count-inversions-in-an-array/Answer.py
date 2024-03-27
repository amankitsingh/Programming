### Answer 1 -Brute force
### TC - O(n^2), SC - O(1)
def numberOfInversions(a : List[int], n : int) -> int:
    # Count the number of pairs:
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] > a[j]:
                cnt += 1
    return cnt

### Answer 2 - Using merge sort
### TC - O(n*nlogn), SC - O(N)
'''
Intuition
If the array is sorted then its easier to find the number of element greater
A1 - [1,2,3]
A2 - [2,3,4,5]
if A1<A2:
    take count
sort and count
'''
def merge(arr : List[int], low : int, mid : int, high : int) -> int:
    temp = []   
    left = low  
    right = mid + 1 
    cnt = 0  
    
    while (left <= mid and right <= high):
        if (arr[left] <= arr[right]):
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            cnt += (mid - left + 1)  #core logic
            right += 1

    while (left <= mid):
        temp.append(arr[left])
        left += 1    
    while (right <= high):
        temp.append(arr[right])
        right += 1
    for i in range(low, high + 1):
        arr[i] = temp[i - low]
    return cnt 

def mergeSort(arr : List[int], low : int, high : int) -> int:
    cnt = 0
    if low >= high:
        return cnt
    mid = math.floor((low + high) / 2)
    cnt += mergeSort(arr, low, mid)
    cnt += mergeSort(arr, mid + 1, high)
    cnt += merge(arr, low, mid, high)
    return cnt

def numberOfInversions(a : List[int], n : int) -> int:
    
    n = len(a)
    
    return mergeSort(a, 0, n - 1)
