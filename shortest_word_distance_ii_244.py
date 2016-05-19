class WordDistance(object):
    def __init__(self, words):
        self.map = dict()
        for i, w in enumerate(words):
            if w in self.map:
                self.map.get(w).append(i)
            else:
                self.map[w] = [i]

    def shortest(self, w1, w2):
        idx1 = self.map.get(w1, [])
        idx2 = self.map.get(w2, [])
        distance = sys.maxint
        i1, i2 = 0, 0
        while i1 < len(idx1) and i2 < len(idx2):
            distance = min(distance, abs(idx1[i1] - idx2[i2]))
            if idx1[i1] < idx2[i2]:
                i1 += 1
            else:
                i2 += 1

        return distance

