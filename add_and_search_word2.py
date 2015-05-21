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
        #corner case
        if word is None:
            if len(self.root.children) == 0:
                return True
            else:
                return False
        bfs_list = []
        bfs_list.append(self.root)
        index = 0
        while len(bfs_list) > 0:
            tmp_list = []
            char = word[index]
            while len(bfs_list) > 0:
                #pop each level elements into a tmp_list
                tmp_list.append(bfs_list.pop())

            while len(tmp_list) > 0:
                tmp_root = tmp_list.pop()
                if char in tmp_root.children.keys():
                    #put
                    bfs_list.insert(0, tmp_root.children.get(char))
                elif char == '.':
                    #add everything into list
                    bfs_list.extend(tmp_root.children.values())
            if index == len(word)-1:
                for i in range(len(bfs_list)):
                    if bfs_list[i].end_of_word:
                        return True
                return False
            index += 1
        return False
