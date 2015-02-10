class solution:
    def singlenumber(self, A):
        return reduce(lambda x, y: x^y, A)

