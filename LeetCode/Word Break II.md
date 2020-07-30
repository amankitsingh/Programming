### Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

### Note:

- The same word in the dictionary may be reused multiple times in the segmentation.
- You may assume the dictionary does not contain duplicate words.

```
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
```
```
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
```
```
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
```

---

### Code:

- I dint solve this
### C++:

```
class Solution {
    unordered_map<string, vector<string>> dp;
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        dp.clear();
        return  help(s,wordDict);
    }
    vector<string> help(string s, vector<string>& wordDict){ 
        if(s.empty())
            return {""};

        if(dp.find(s)!=dp.end())
            return dp[s];

        vector<string>subpart,wholepart;
        for(string word : wordDict){
            string igot = s.substr(0,word.length());

            if(igot != word){
                continue ; 
            }else{
                subpart = help(s.substr(word.length()) , wordDict);
            }

            for(string ans : subpart){
                string space = ans.length()==0 ? "" : " ";
                wholepart.push_back(word+space+ans);
            }
        }

        return dp[s] = wholepart;
    }

};
```
