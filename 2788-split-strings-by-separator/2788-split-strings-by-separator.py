class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []
        for word in words:
            temp = [x.strip() for x in word.split(separator) if x]
            result.extend(temp)
        return result