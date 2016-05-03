class ZigzagIterator(object):

    def __init__(self, lists):
        self.iter_list = []
        for l in lists:
            if l:
                self.iter_list.append(iter(l))
        self.turns = 0

    def next(self):
        if not self.hasNext():
            raise StopIteration('no next value')
        else:
            index = self.turns % len(self.iter_list)
            iterator = self.iter_list[index]
            res = next(iterator, None)
            if next(iterator, None) is None:
                del self.iter_list[index]
                self.turns = index-1
            self.turns += 1
            return res

    def hasNext(self):
        if len(self.iter_list) > 0:
            return True
        return False



s = ZigzagIterator([[1,2,3]])
print s.hasNext()
print s.next()
