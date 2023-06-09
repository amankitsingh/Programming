class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for x in range(len(arr)):
            if 2*arr[x] in seen:
                return True
            elif arr[x]%2 == 0 and arr[x]/2 in seen:
                return True
            else:
                seen.add(arr[x])
        return False