ass Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        firstOfLine = True
        # list of lines 
        lineLists = []
        curL = 0
        k = 0
        while k < len(words):
            word = words[k]
            if firstOfLine:
                line = []
                if len(word) <= maxWidth:
                    line.append(word)
                    lineLists.append(line)
                    curL += len(word)
                    firstOfLine = False
                    k += 1
                else:
                    return []
            else:
                if curL + len(word) + 1 <= maxWidth:
                    lineLists[-1].append(' ')
                    lineLists[-1].append(word)
                    curL += len(word) + 1
                    k += 1
                else:
                    diff = maxWidth - curL
                    # special case one word
                    if len(lineLists[-1]) == 1:
                        lineLists[-1].append(' ' * diff)
                    else:
                        i = 1
                        while diff > 0:
                            if i >= len(lineLists[-1]):
                                i = 1
                            lineLists[-1][i] = lineLists[-1][i] + ' '
                            i += 2
                            diff -= 1
                    # reset
                    firstOfLine = True
                    curL = 0
        # check last line, make sure space is arranged properly
        diff = maxWidth - curL
        # special case one word
        lineLists[-1].append(diff * ' ')
        
        lines = []
        for lineList in lineLists:
            lines.append(''.join(lineList))
        return lines
