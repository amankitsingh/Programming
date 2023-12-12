class Solution:
    def parseBoolExpr(self, expression: str, t=True, f=False) -> bool:
        return eval(expression.replace('!', 'not |').replace('&(', 'all([').replace('|(', 'any([').replace(')', '])'))
                
            