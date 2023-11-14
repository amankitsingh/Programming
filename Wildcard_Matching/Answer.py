### Answer 1
### Time complexity - O(N*M), Space complexity - O(N*M) + O(N+M)
def wildcardMatching(pattern, text):
    pattern = pattern.strip()
    text = text.strip()
    lenofpattern = len(pattern)
    lenoftext = len(text)
    dp = [[-1 for _ in range(lenoftext+1)] for _ in range(lenofpattern+1)]
    
    # helper function
    def isAllStars(i):
        for j in range(i+1):
            if pattern[j]!="*":
                return False
        return True
        
    def findpattern(indexp, indext):
        # Base condititon
        if indexp < 0 and indext < 0:
            return True
        elif indexp < 0 and indext >= 0:
            return False
        if indexp >= 0 and indext < 0:
            return isAllStars(indexp)

        if dp[indexp][indext] != -1:
            return dp[indexp][indext]
            
        if pattern[indexp] == text[indext] or pattern[indexp] == "?":
            dp[indexp][indext] = findpattern(indexp - 1, indext - 1)
        elif pattern[indexp] == "*":
            dp[indexp][indext] = findpattern(indexp-1, indext) or findpattern(indexp, indext - 1)
        else:
            dp[indexp][indext] = False

        return dp[indexp][indext]
        
    return findpattern(lenofpattern - 1, lenoftext - 1)
