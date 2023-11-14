```
We are given two strings ‘S1’ and ‘S2’. String S1 can have the following two special characters:

‘?’ can be matched to a single character of S2.
‘*’ can be matched to any sequence of characters of S2. (sequence can be of length zero or more).
We need to check whether strings S1 and S2 match or not.
```
Example

```
Sample Input 1:
3
?ay
ray
ab*cd
abdefcd
ab?d
abcc
Sample Output 1:
True
True
False
```
