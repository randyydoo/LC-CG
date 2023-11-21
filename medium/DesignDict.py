class TrieNode:
    def __init__(self):
        self.children = {}  
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]


        node.word = True

    def search(self, word: str) -> bool:
        def dfs(i,root):
            if not root:
                return
            elif i == len(word):
                return root.word

            if word[i] == '.':
                for v in root.children.values():
                    if dfs(i+1,v):
                        return True
            elif word[i] in root.children:
                return dfs(i+1,root.children[word[i]])
                
        return dfs(0,self.root)
