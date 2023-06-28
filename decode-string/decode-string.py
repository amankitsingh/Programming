from collections import deque
class Solution:
    def decodeString(self, s: str) -> str:
        decoding_stack = deque()
        temp = deque()
        for i in s:
            if i == "]":
                multiple=""
                while len(decoding_stack[-1]) > 1 or not (48<= ord(decoding_stack[-1])<=57):
                    temp.appendleft(decoding_stack.pop())
                temp.popleft()
                while decoding_stack and not len(decoding_stack[-1]) > 1 and (48<= ord(decoding_stack[-1])<=57):
                    multiple += decoding_stack.pop()
                multiple = multiple[::-1]
                decoding_stack.append(''.join(temp)*int(multiple))
                temp = deque()
                multiple = ""
            else:
                decoding_stack.append(i)
        return ''.join(decoding_stack)

#Answer 2
class Solution:
    def decodeString(self, s: str) -> str:
        numStack = []
        strStack = []
        curNum = []
        curStr = ""
        for char in s:
            if char.isdigit():
                curNum.append(char)
            elif char == "[":
                numStack.append(int("".join(curNum)))
                strStack.append(curStr)
                curStr = ""
                curNum = []
            elif char == "]":
                lastNum = numStack.pop()
                lastStr = strStack.pop()
                curStr = lastStr + curStr * lastNum
            else:
                curStr += char
        return curStr

#Answer 3
class Solution:
    def decodeString(self, s):
        while '[' in s:
            s = re.sub(r'(\d+)\[([a-z]*)\]', lambda m: int(m.group(1)) * m.group(2), s)
        return s

