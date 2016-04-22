class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        # find shortest path
        # bfs
        # since there are only 26 characters, we can try each location with all char
        level = 1
        if beginWord == endWord:
            return level
        prevLevel = collections.deque()
        prevLevel.append([beginWord, 1])
        wordList.add(endWord)
        while prevLevel:
            l = prevLevel.popleft()
            cur = l[0]
            curL = l[1]
            if cur == endWord:
                return curL
            for j in xrange(len(beginWord)):
                for k in 'abcdefghijklmnopqrstuvwxyz':
                    if k != cur[j]:
                        word = cur[:j] + k + cur[j+1:]
                        if word in wordList:
                            prevLevel.append([word, curL+1])
                            wordList.remove(word)
        return 0
        
            
                    
                
# reference: http://bookshadow.com/weblog/2015/08/17/leetcode-word-ladder/        
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordDict):
        from collections import defaultdict, deque
        qf = deque( [ [beginWord, 0] ] )
        qe = deque( [ [endWord, 0] ] )
        sf = { }
        se = { }
        neighbors = defaultdict(list)
        for word in wordDict:
            for x in range(len(word)):
                token = word[:x] + '_' + word[x+1:]
                neighbors[token] += word,
        while qf or qe:
            if qf:
                word, length = qf.popleft()
                if word in se :
                    return length + se[word] + 1
                for x in range(len(word)):
                    token = word[:x] + '_' + word[x+1:]
                    for ladder in neighbors[token]:
                        if ladder not in sf:
                            sf[ladder] = length + 1
                            qf += [ladder, length + 1],
            if qe:
                word, length = qe.popleft()
                if word in sf :
                    return length + sf[word] + 1
                for x in range(len(word)):
                    token = word[:x] + '_' + word[x+1:]
                    for ladder in neighbors[token]:
                        if ladder not in se:
                            se[ladder] = length + 1
                            qe += [ladder, length + 1],
        return 0
                    
# reference: https://leetcode.com/discuss/48083/share-python-solutions-concise-160ms-optimized-solution-100ms
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordDict):
        front, back=set([beginWord]), set([endWord])
        length=2
        width=len(beginWord)
        charSet=list(string.lowercase)
        wordDict.discard(beginWord)
        wordDict.discard(endWord)
        while front:
            newFront=set()
            for phrase in front:
                for i in xrange(width):
                    for c in charSet:
                        nw=phrase[:i]+c+phrase[i+1:]
                        if nw in back:
                            return length
                        if nw in wordDict:
                            newFront.add(nw)
            front=newFront
            if len(front)>len(back):
                front,back=back,front
            wordDict-=front
            length+=1
        return 0        
               
