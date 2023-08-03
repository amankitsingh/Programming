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

class Solution:
    def generateParenthesis(self, n):
        if not n:
            return []
        left, right, ans = n, n, []
        self.dfs(left,right, ans, "")
        return ans

    def dfs(self, left, right, ans, string):
        if right < left:
            return
        if not left and not right:
            ans.append(string)
            return
        if left:
            self.dfs(left-1, right, ans, string + "(")
        if right:
            self.dfs(left, right-1, ans, string + ")")
                
