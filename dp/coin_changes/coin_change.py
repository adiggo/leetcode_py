#param m: data size
#param n: target value
def count(data, m, n):
    if n == 0:
        return 1
    if m <= 0:
        return 0
    if n < 0:
        return 0
    return count(data, m-1, n) + count(data, m, n-data[m-1])

# there are two kind of solution: one include current data, another exclude current data.

#params same as above. But this one store all results in array so we can avoid overlap problem.
def get_num(data, m, n):
    helper = [[0 for x in range(m)] for x in range(n + 1)]
    # initial value set up
    for i in range(m):
        helper[0][i] = 1

    for i in range(1, n+1):
        for j in range(m):
            # include current data 
            x = helper[i-data[j]][j] if i- data[j] >= 0 else 0
            # exclude current data
            y = helper[i][j-1] if j >=1 else 0
            helper[i][j]=x+y
    return helper[n][m-1]

print get_num([1,2,3],3,4)
