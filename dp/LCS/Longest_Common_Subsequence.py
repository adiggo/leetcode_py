

# optimal substructure
def get_longest_common_sequence(s1, s2):
    
    if not s1 or not s2:
        return 0
    
    helper = [[0 for x in range(len(s1)+1)] for x in range(len(s2)+1)]
    # since current value in helper is based on i-1 and j-1, which means we need some initialized value for i == 0 and j== 0 situation. 
    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if i == 0 or j == 0:
                continue
            if s1[i-1] == s2[j-1]:
                helper[i][j] = 1 + helper[i-1][j-1]
            else:
                helper[i][j] = max(helper[i][j-1], helper[i-1][j])
    return helper[len(s1)][len(s2)]
