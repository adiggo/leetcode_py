class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.children = dict()
        self.end_of_word = False

class WordDictionary:

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        tmp_root = self.root
        for char in word:
             if char not in tmp_root.children:
                 tmp_root.children[char] = TrieNode()
                 tmp_root = tmp_root.children.get(char)
             else:
                 tmp_root = tmp_root.children.get(char)
        tmp_root.end_of_word = True
            
    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        #corner case
        if not word:
            return True
        return self.dfs(word, 0, self.root)
        
    def dfs(self, word, start, node):
        if start == len(word):
            return node.end_of_word
        if word[start] in node.children:
            if self.dfs(word, start+1, node.children.get(word[start])):
                return True
            else:
                return False
        elif word[start] == '.':
            for c in node.children:
                if self.dfs(word, start+1, node.children.get(c)):
                    return True
            return False
        else:
            return False
        return False
