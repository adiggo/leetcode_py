class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        #constant search time if we set children into a dict. The key is the char
        self.children = dict()
        self.end_of_word = False
        

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        tmp_root = self.root
        for char in word:
             if tmp_root.children.get(char) is None:
                 tmp_root.children[char] = TrieNode()
                 tmp_root = tmp_root.children.get(char)
             else:
                 tmp_root = tmp_root.children.get(char)
        tmp_root.end_of_word = True
                

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        tmp_root = self.root
        for char in word:
            tmp_root = tmp_root.children.get(char)
            if tmp_root is None:
                return False
        return tmp_root.end_of_word

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        tmp_root = self.root
        for char in prefix:
            tmp_root = tmp_root.children.get(char)
            if tmp_root is None:
                return False
        return True
