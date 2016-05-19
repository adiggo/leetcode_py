def shortest_distance(words, w1, w2):
    i1, i2 = -1, -1
    distance = sys.maxint
    for i in xrange(len(words)):
        if words[i] == w1:
            i1 = i
            if i2 != -1:
                distance = min(distance, i1 - i2)
        if words[i] == w2:
            i2 = i
            if i1 != -1:
                distance = min(distance, i2 - i1)
    return distance

