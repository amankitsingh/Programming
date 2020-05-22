### Given a string, sort it in decreasing order based on the frequency of characters.

```
Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
```
```
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
```
```
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
```
---
## Code:
### python way
```
import collections
class Solution:
    def frequencySort(self, s: str) -> str:
        x=collections.Counter(s)
        x=sorted(x.items(), key=lambda y: y[1],reverse=True)
        s=""
        for k,v in x:
            if v>1:
                s=s+(k*v)
            else:
                s=s+k    
        return s
        
```
### C++

- 1st way
```
class Solution {
public:
    int countFrequency(string str, char ch) 
    { 
        int count = 0; 
         for (int i = 0; i < str.length(); i++) 
            if (str[i] == ch) 
                 ++count;
        return count; 
    } 
    static bool sortinrev(const pair<int,char> &a,  
               const pair<int,char> &b) 
    { 
       return (a.first > b.first); 
    } 
    string frequencySort(string str) {
        int n = str.length();
        string s;
        vector<pair<int, char>> vp; 
          for (int i = 0; i < n; i++) { 
            vp.push_back( 
                make_pair( 
                    countFrequency(str, str[i]), 
                    str[i])); }
        sort(vp.begin(), vp.end(),sortinrev);
        for(int i=0;i<vp.size();i++)
            s=s+vp[i].second;
        return s;
    }
};
```
- 2nd way
```
class Solution {
public:
    string frequencySort(string s) {
    vector <int> dat;
    vector <pair <int, int> > freq;
        dat.assign(256, 0);
        for(auto x: s)
            dat[x]++;
        for(int i = 0; i < dat.size(); i++)
            if(dat[i])
                freq.push_back({-dat[i], i});
        sort(freq.begin(), freq.end());
        string result = "";
        for(auto kv: freq)
            result += string(-kv.first, kv.second);
        return result;
    }
};
        

```
