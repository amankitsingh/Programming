class Solution:
    def reversePairs(self, a: List[int]) -> int:
        def merge(arr : List[int], low : int, mid : int, high : int) -> int:
            temp = []   # temporary array
            left = low  # starting index of left half of arr
            right = mid + 1 # starting index of right half of arr

            cnt = 0     # Modification 1: cnt variable to count the pairs

            # storing elements in the temporary array in a sorted manner
            while (left <= mid and right <= high):
                if (arr[left] <= arr[right]):
                    temp.append(arr[left])
                    left += 1
                else:
                    temp.append(arr[right])
                    cnt += (mid - left + 1)  # Modification 2
                    right += 1

            # if elements on the left half are still left
            while (left <= mid):
                temp.append(arr[left])
                left += 1

            # if elements on the right half are still left
            while (right <= high):
                temp.append(arr[right])
                right += 1

            # transfering all elements from temporary to arr
            for i in range(low, high + 1):
                arr[i] = temp[i - low]

            return cnt   # Modification 3

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
        # Count the number of pairs:
        return mergeSort(a, 0, n - 1)