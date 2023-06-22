class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        expression = ["+", "-", "*", "/"]
        for x in tokens:
            if x in expression:
                second = int(stack.pop())
                first = int(stack.pop())
                match x:
                    case "+":
                        stack.append(first+second)
                    case "-":
                        stack.append(first-second)
                    case "*":
                        stack.append(first*second)
                    case "/":
                        stack.append(first/second)
                        '''
                        if first < 0 or second < 0:
                            stack.append(math.ceil(first/second))
                        else:
                            stack.append(math.floor(first/second))
                        '''
            else:
                stack.append(x)
        return int(stack[0])