
#input is an array
#running time is O(n^2)
def get_longest_sequence(A):
    if not A:
        return None

    helper = [1] * len(A)
    
    for i in range(1, len(A)):
        for j in range(0, i):
            # suppose we need strictly increasing subsequence
            if helper[i] < helper[j] + 1  and  A[i] > A[j]:
                helper[i] = helper[j] + 1
        
    res = 1
    for i in helper:
        res = max(i, res)
    return res

