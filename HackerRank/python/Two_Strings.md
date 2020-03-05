## Two Strings
---
```
Given two strings, determine if they share a common substring. A substring may be as small as one character.

For example, the words "a", "and", "art" share the common substring . The words "be" and "cat" do not share a substring.
```
---
### Sample Input:
```
2
hello
world
hi
world
```
### Sample Output:
```
YES
NO
```
---
### Code:

```
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def twoStrings(s1, s2):
    st1=Counter(s1)
    st2=Counter(s2)
    t= "NO"
    for x in st1:
        if x in st2:
           t = "YES" 
    return t

q = int(input())
for q_itr in range(q):
  s1 = input()
  s2 = input()
result = twoStrings(s1, s2)
```
