class Solution:
    def generateParenthesis(self, n):
        result = []
        stack = []
        def backtrace(openp, closep):
            if openp == closep == n:
                result.append("".join(stack))
                return
            if openp < n:
                stack.append("(")
                backtrace(openp+1,closep)
                stack.pop()
            if closep < openp:
                stack.append(")")
                backtrace(openp, closep+1)
                stack.pop()
        backtrace(0,0)
        return result
                