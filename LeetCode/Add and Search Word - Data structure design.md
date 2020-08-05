### Design a data structure that supports the following two operations:

- void addWord(word)
- bool search(word)
- search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

```
Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
```
### Note:
- You may assume that all words are consist of lowercase letters a-z.

- Use tries

### Code:

### C++:

```
class WordDictionary {
    WordDictionary* child[26];
    bool isEnd;
public:
    /** Initialize your data structure here. */
    WordDictionary() {
        ios::sync_with_stdio(0);
        cin.tie(0);
        isEnd = false;
        for(int i=0;i<26;++i)
            child[i] = nullptr;
    }
    
    /** Adds a word into the data structure. */
    void addWord(string word) {
        WordDictionary* temp = this;
        for(char c: word){
            
            if(!temp->child[c-'a'])
                temp->child[c-'a'] = new WordDictionary;
            temp = temp->child[c-'a'];
        }
        temp->isEnd = true;
    }
    
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    bool search(string word) {
        WordDictionary* temp = this;
        for(int i=0;i<word.length();++i){
            char c = word[i];
            if(c == '.'){
                for(auto ch:temp->child)
                    if( ch && ch->search(word.substr(i+1))) return true;
                return false;
            }
            if(! temp->child[c-'a'])
                return false;
            temp = temp->child[c-'a'];
            
        }
        return temp->isEnd;
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */
```

### Python:

```
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = [None]*26
        self.isEnd = False
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self
        for c in word:
            if curr.children[ord(c)-ord('a')] == None:
                curr.children[ord(c)-ord('a')] = WordDictionary()
            curr = curr.children[ord(c)-ord('a')]
        curr.isEnd = True;

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        curr = self
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                for ch in curr.children:
                    if ch != None and ch.search(word[i+1:]): return True
                return False
            
            if curr.children[ord(c) - ord('a')] == None: return False
            curr = curr.children[ord(c) - ord('a')]
        
        return curr != None and curr.isEnd
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```

### Other way:

```
class WordDictionary(object):
    def __init__(self):
        self.word_dict = collections.defaultdict(list)
        self.wordSet = set()
        

    def addWord(self, word):
        if word:
            self.word_dict[len(word)].append(word)
            self.wordSet.add(word)

    def search(self, word):
        if word in self.wordSet:
            return True
        else:
            for v in self.word_dict[len(word)]:
                # match xx.xx.x with yyyyyyy
                for i, ch in enumerate(word):
                    if ch != v[i] and ch != '.':
                        break
                else:
                    return True
            return False
        
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```
