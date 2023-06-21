class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures: return []
        result, stack = [0] * len(temperatures), []
        stack.append((temperatures[0], 0))
        
        for i in range(1, len(temperatures)):
            while stack:
                prev = stack[-1]
                if prev[0] < temperatures[i]:
                    result[prev[1]] = i - prev[1]
                    stack.pop()
                else:
                    break
            stack.append((temperatures[i], i))
        return result