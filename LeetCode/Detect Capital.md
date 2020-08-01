### Given a word, you need to judge whether the usage of capitals in it is right or not.

### We define the usage of capitals in a word to be right when one of the following cases holds:

- All letters in this word are capitals, like "USA".
- All letters in this word are not capitals, like "leetcode".
- Only the first letter in this word is capital, like "Google".
- Otherwise, we define that this word doesn't use capitals in a right way.

```
Example 1:

Input: "USA"
Output: True
``` 

```
Example 2:

Input: "FlaG"
Output: False
``` 

- Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.

### Code:

### C++:

```
class Solution {
public:
    bool detectCapitalUse(string word) {
        bool match1=true,match2=true,match3=true;
        int n = word.size();
        for(int i=0;i<n;i++){
            if(!isupper(word[i])){
                match1 = false;
                break;
            }
        }
        if(match1)
            return true;
        
        for(int i=0;i<n;i++){
            if(isupper(word[i])){
                match2 = false;
                break;
            }
        }
        if(match2)
            return true;
        
        if(!isupper(word[0]))
            match3 = false;
        
        if(match3)
            for(int i=1;i<n;i++){
                if(isupper(word[i]))
                    match3 = false;
            }
        
        if(match3)
            return true;
        return false;
    }
};
```

### Other way:

```
class Solution {
public:
    bool detectCapitalUse(string word) {
     
       
        int flag = 0;
        for(int i = 0 ; i < word.size() ; i++)
        {
            if(word[i] >= 97 && word[i] <= 122 && flag == 1)
                return false;
            if(word[i] >= 65 && word[i] <= 90 && flag == 0)
            {
                if(i==1)
                {
                    if(word[0] >= 65 && word[0] <= 90)
                    {
                        flag = 1;
                    }
                    else
                        return false;
                }
                else if(i > 1)
                {
                    if(flag != 1)
                        return false;
                }
            }
                
        }
        return true;
        
    }
};
```

### Python:

```
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.istitle() or word.isupper() or word.islower():
            return True
        return False
```
