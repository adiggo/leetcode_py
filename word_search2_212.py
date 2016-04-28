class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        if not words:
            return []
        if not board:
            return []
        trie = Trie()
        for word in words:
            trie.insert(word)
        m, n = len(board), len(board[0])
        visited = [[False] * n for x in range(m)]
        for i in xrange(m):
            for j in xrange(n):
                self.back_track(board, board[i][j], i, j, trie.root, visited, res, trie)
        return res

    def back_track(self, board, word, i, j, parent, visited, ans, trie):
        node = parent.childs.get(board[i][j])
        if node is None:
            return
        m, n = len(board), len(board[0])
        # four direction
        visited[i][j] = True
        if i + 1 < m and not visited[i + 1][j]:
            self.back_track(board, word + board[i+1][j], i + 1, j, node, visited, ans, trie)
        if j - 1 >= 0 and not visited[i][j - 1]:
            self.back_track(board, word + board[i][j-1], i, j - 1, node, visited, ans, trie)
        if i - 1 >= 0 and not visited[i - 1][j]:
            self.back_track(board, word + board[i-1][j], i - 1, j, node, visited, ans, trie)
        if j + 1 < n and not visited[i][j + 1]:
            self.back_track(board, word + board[i][j+1], i, j + 1, node, visited, ans, trie)
        if node.isWord:
            ans.append(word)
            trie.delete(word)
        visited[i][j] = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        node = self.root
        for letter in word:
            child = node.childs.get(letter)
            if child is None:
                child = TrieNode()
                node.childs[letter] = child
            node = child
        node.isWord = True

    def delete(self, word):
        node = self.root
        queue = []
        for letter in word:
            queue.append((letter, node))
            child = node.childs.get(letter)
            if child is None:
                return False
            node = child
        if not node.isWord:
            return False
        if len(node.childs):
            node.isWord = False
        else:
            for letter, node in reversed(queue):
                del node.childs[letter]
                if len(node.childs) or node.isWord:
                    break
        return True
        
class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.childs = dict()
        self.isWord = False
