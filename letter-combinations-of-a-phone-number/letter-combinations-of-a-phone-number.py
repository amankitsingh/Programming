class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_number_comb = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                            "6": "mno", "7": "pqrs", "8": "tuv", "9" : "wxyz"}
        
        if len(digits) == 0:
            return []
        result = []
        def backtrace(start, comb):
            if len(comb) == len(digits):
                result.append("".join(comb[:]))
                return
            
            for i in range(start,len(digits)):
                value = phone_number_comb[digits[i]]
               
                for alp in value:
                    comb.append(alp)
                    backtrace(i+1, comb)
                    comb.pop()
        for i in phone_number_comb[digits[0]]:
            backtrace(1, [i])
        return result