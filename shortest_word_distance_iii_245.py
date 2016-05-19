def shortest_distance(words, w1, w2):
    i1, i2 = -1, -1
    distance = sys.maxint
    inc = 1 if w1 == w2 else 0
    turn = 0
    for i in xrange(len(words)):
        if words[i] == w1 and turn % 2 == 0:
            i1 = i
            if i2 != -1:
                distance = min(distance, i1 - i2)
            turn += inc
        elif words[i] == w2:
            i2 = i
            if i1 != -1:
                distance = min(distance, i2 - i1)
            turn += inc
    return distance
