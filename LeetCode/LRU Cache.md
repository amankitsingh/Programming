### Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

- get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
- put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

### The cache is initialized with a positive capacity.

### Follow up:
- Could you do both operations in O(1) time complexity?

```
Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
```

---

### Code:

### C++:

```
class LRUCache {

    struct Node {
        int val;
        int key;
        Node* prev;
        Node* next;
        
        Node(int key,int val){
            
            this->key = key;
            this->val = val;
            prev = nullptr;
            next = nullptr;
        }
    };
    
    unordered_map<int,Node*> mp;
    Node* front = nullptr;
    Node* rear = nullptr;
    int csize = 0;
public:
    LRUCache(int capacity) {
        this->csize = capacity;
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
    }
    
    int get(int key) {
        
        auto it = mp.find(key);
        
        if(it == mp.end())
            return -1;
        else {
            Node* t = it->second;
            if(t == this->front)
                return t->val;
            t->prev->next = t->next;
            if(t != rear)
                t->next->prev = t->prev;
            else 
                this->rear = t->prev;
            t->next = this->front;
            t->prev = nullptr;
            this->front->prev = t;
            this->front = t;
            
            return t->val;
        }
    }
    
    void put(int key, int value) {
        if(mp.size() == 0){
            Node* temp = new Node(key,value);
            this->front = temp;
            this->rear = temp;
            mp[key] = temp;
            return;
        }
        
        auto it = mp.find(key);
        if(it != mp.end()){
            Node* t = it->second;
            if(t->val != value){
                t->val = value;
                if(t == this->front){
                    return;
                }
                
                t->prev->next = t->next;
                
                if(t != this->rear)
                    t->next->prev = t->prev;
                else
                    this->rear = t->prev;
                t->next = this->front;
                t->prev = nullptr;
                this->front->prev = t;
                this->front = t;
            }
            return;
        }
        
        if(mp.size() < csize){
            
            Node* t = new Node(key,value);
            t->next = this->front;
            this->front->prev = t;
            this->front = t;
            mp[key] = t;
            
        } else if (mp.size() == csize){
            
            Node* t = this->rear;
            this->rear = this->rear->prev;
            
            mp.erase(t->key);
            delete(t);
            
            Node* temp = new Node(key,value);
            if(mp.size() == 0){
                this->front = temp;
                this->rear = temp;
                mp[key] = temp;
            } else {
                this->front->prev = temp;
                temp->next =  this->front;
                this->front = temp;
                mp[key] = temp;
            }
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
```
