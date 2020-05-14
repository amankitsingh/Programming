## Implement a trie with insert, search, and startsWith methods.

```
Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
```

### Note:

### You may assume that all inputs are consist of lowercase letters *a-z*.
### All inputs are guaranteed to be non-empty strings.
---
Code:

```
class Trie {
    Trie* child[26];
    bool isEnd;
public:
    /** Initialize your data structure here. */
    Trie() {
        ios::sync_with_stdio(0);
        cin.tie(0);
        isEnd = false;
        for(int i=0;i<26;++i)
            child[i] = nullptr;
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        Trie* temp = this;
        for(char c:word)
        {
            if (!(temp->child[c - 'a']))
                temp->child[c - 'a'] = new Trie;
            temp = temp->child[c -'a'];

        }
        temp->isEnd=true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        Trie* temp = this;
        for(char c:word)
        {
            if(! temp->child[c-'a'])
                return false;
            temp = temp->child[c-'a'];
        }
        return(temp->isEnd);
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        Trie* temp = this;
        for(char c:prefix)
        {
           
            if(! temp->child[c-'a'])
                return false;
             temp = temp->child[c-'a'];
        }
        return true;
    }
};
```
