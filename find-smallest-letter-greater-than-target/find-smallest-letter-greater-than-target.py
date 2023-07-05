class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        first,last = 0, len(letters) - 1
        mid = inf        
        while first < last:
            mid = (first+last) >> 1
            if ord(letters[mid]) > ord(target):
                last = mid
            else:
                first = mid + 1
                
        return letters[0] if letters[first] == letters[last] and ord(letters[first]) <= ord(target) else letters[first]