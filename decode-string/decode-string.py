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


