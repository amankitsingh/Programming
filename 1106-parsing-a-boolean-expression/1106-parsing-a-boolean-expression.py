### Answer 1
### Time complexity - O(N), Space complexity - O(N)
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        operator = ["&","|","!"]
        operands = ["t","f"]
        
        stack = []
        
        for i in expression:
            if i == ")":
                temp = []
                temp.append(stack.pop())
                for k in range(len(stack)-1, 0,-1):
                    if stack[k] != "(":
                        temp.append(stack.pop())
                    else:
                        stack.pop() #remove the first open bracket
                        break
                exper = stack.pop()
                if exper == "!":
                    stack.append("f" if "t" in temp else "t")
                elif exper == "&":
                    stack.append("f" if "f" in temp else "t")
                elif exper == "|":
                    stack.append("t" if "t" in temp else "f")
            elif i != ",":
                stack.append(i)
        
        return stack[0] == "t"
    

### dont try in interview
### all - and , any - or
class Solution:
    def parseBoolExpr(self, expression: str, t=True, f=False) -> bool:
        return eval(expression.replace('!', 'not |').replace('&(', 'all([').replace('|(', 'any([').replace(')', '])'))
