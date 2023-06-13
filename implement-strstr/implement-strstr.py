class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        firstoccur,lenneedle = -1, len(needle)
        for i in range(len(haystack)):
            print(haystack[i:i+lenneedle])
            if haystack[i] == needle[0] and haystack[i:i+lenneedle] == needle:
                firstoccur = i
                break
        return firstoccur    
    
    
'''
"sadbutsad"
"sad"
"leetcode"
"leeto"
"ankit"
"akki"
'''