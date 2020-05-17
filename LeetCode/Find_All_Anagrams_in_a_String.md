### Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

### Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

### The order of output does not matter.
```
Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

```
```
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
```
---
### Code:
```
class Solution {
    
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> res;
        int n = s.size(), m = p.size();
        //if(n<m)   return res;
        //if(n==0||m==0)  return res;
        vector<int> ar(26, 0);
        for(auto c : p) {
            ++ar[c - 'a'];
        }
        int count = m, currLen = 0, start = 0;
        for(int i = 0;i<n;i++) {
            
            if (ar[s[i] - 'a']-- > 0) --count;
            
            while (count == 0) {
                currLen = i - start + 1;
                if (currLen == m) {
                    res.push_back(start);
                }
                if (ar[s[start++] - 'a']++ == 0)
                    ++count;
            }
            
        }
        return res;
    }
};


static int __ = []() {
	std::ios::sync_with_stdio(false);
	std::cin.tie(nullptr);
	std::cout.tie(nullptr);
	return 0;
}();

```
