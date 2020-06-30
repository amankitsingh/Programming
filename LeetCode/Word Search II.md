### Given a 2D board and a list of words from the dictionary, find all words in the board.

### Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

```
Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
``` 

### Note:

- All inputs are consist of lowercase letters a-z.
- The values of words are distinct.

### Hint 1:

- You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?

### Hint 2:

- If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.

---

### Code:

```
class Trie {
public:
    Trie* children[26];
    bool endofWord;
    Trie():endofWord(false){
        for(int i=0;i<26;++i)
            children[i]=nullptr;
    }
    ~Trie(){
        for(int i=0;i<26;++i)
            if(children[i]) delete children[i];
    }
    void insert(string word){
        Trie* curr = this;
        for(char c: word){
            if(curr->children[c-'a']==nullptr) curr->children[c-'a'] = new Trie();
            curr = curr->children[c-'a'];
        }
        curr->endofWord = true;
    }
};
class Solution {
    void dfs(vector<vector<char>>& board,int i,int j, unordered_set<string>& result,Trie* trie,string word){
        char c = board[i][j];
        if(c=='$') return;
        board[i][j] = '$';
        Trie* t = trie->children[c-'a'];
        if(t){
            string ss = word+c;
            if(t->endofWord) result.insert(ss);
            if(i < board.size()-1) dfs(board,i+1,j,result,t,ss);
            if(j < board[0].size()-1) dfs(board,i,j+1,result,t,ss);
            if(i > 0) dfs(board,i-1,j,result,t,ss);
            if(j>0) dfs(board,i,j-1,result,t,ss);            
        }
        board[i][j] = c;
    }
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        if(words.size()==0)
            return {};
        Trie trie;
        for(string w:words) trie.insert(w);
        
        unordered_set<string> result;
        for(int i=0;i<board.size();++i)
            for(int j=0;j<board[0].size();++j)
                dfs(board,i,j,result,&trie,"");
        
        vector<string> result_final(result.begin(),result.end());
        
        return result_final;
    }
};
```
