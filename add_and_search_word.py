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
             if tmp_root.children.get(char) is None:
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
        return dfs(word, self.root.children, 0)

def dfs(word, children, index):
    #special/corner case
    if index == len(word):
        if len(children) == 0:
            return True
        else:
            return False
    #get the most left char
    char = word[index]
    if char in children:
        if index == len(word) - 1 and children.get(char).end_of_word == True:
            return True
        return dfs(word, children.get(char).children, index + 1)
    elif char == '.':
        result = False
        for child_node in children.values():
            if index == len(word) - 1 and child_node.end_of_word == True:
                return True
            if dfs(word, child_node.children, index+1) == True:
                result = True
        return result
    else:
        return False
