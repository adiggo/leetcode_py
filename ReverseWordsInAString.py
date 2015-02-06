def reverseWords(self, s):
    g = s.split()
    g = g[::-1]
    res = ""
    for i in range(len(g)):
        res += g[i]
        if i != len(g) - 1:
            res += " "
    return res
