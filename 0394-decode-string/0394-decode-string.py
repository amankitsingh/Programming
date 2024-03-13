from collections import deque
class Solution:
    def decodeString(self, s):
        res,num = "",0
        st = []
        for c in s:
            if c.isdigit():
                num = num*10+int(c)    
            elif c=="[":
                st.append(res)
                st.append(num)
                res=""
                num=0
            elif c=="]":
                pnum = st.pop()
                pstr = st.pop()
                res = pstr + pnum*res
            else:
                res+=c

        return res