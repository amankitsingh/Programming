### Answer - Using merge sort
### TC - O(2*NlogN), SC - O(N)
class Solution:
    def reversePairs(self, a: List[int]) -> int:
        def merge(arr : List[int], low : int, mid : int, high : int) -> int:
            temp = [] 
            left = low  # starting index of left half of arr
            right = mid + 1 # starting index of right half of arr

            while (left <= mid and right <= high):
                if (arr[left] <= arr[right]):
                    temp.append(arr[left])
                    left += 1
                else:
                    temp.append(arr[right])
                    right += 1

            while (left <= mid):
                temp.append(arr[left])
                left += 1

            while (right <= high):
                temp.append(arr[right])
                right += 1

            for i in range(low, high + 1):
                arr[i] = temp[i - low]

        def countPairs(arr, low, mid, high):
            right = mid + 1
            cnt = 0
            for i in range(low, mid + 1):
                while right <= high and arr[i] > 2 * arr[right]:
                    right += 1
                cnt += (right - (mid + 1))
            return cnt

        def mergeSort(arr : List[int], low : int, high : int) -> int:
            cnt = 0
            if low >= high:
                return cnt
            mid = math.floor((low + high) / 2)
            cnt += mergeSort(arr, low, mid)    # left half
            cnt += mergeSort(arr, mid + 1, high)  # right half
            cnt += countPairs(arr, low, mid, high)
            merge(arr, low, mid, high)  # merging sorted halves
            return cnt

        n = len(a)
        return mergeSort(a, 0, n - 1)
