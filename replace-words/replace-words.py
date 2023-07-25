class Solution:
    def __init__(self):
        self.children = {}
        self.isRoot = False
        self.word = None
    
    def insert(self,word):
        head = self
        for c in word:
            if c not in head.children:
                head.children[c] = Solution()
            head=head.children[c]
        head.isRoot = True
        head.word = word
        
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for root_word in dictionary:
            self.insert(root_word)
        
        answer_sentence = []
        for word in sentence.split(" "):
            head = self
            if word[0] in head.children:
                for c in word:
                    if c in head.children and head.isRoot == False:
                        head = head.children[c]
                    else:
                        break
                if head.isRoot:
                    answer_sentence.append(head.word)
                else:
                    answer_sentence.append(word)
            else:
                answer_sentence.append(word)
        return " ".join(answer_sentence)
                        