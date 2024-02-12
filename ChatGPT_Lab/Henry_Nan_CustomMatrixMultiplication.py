def complex_operation(a, b):
    result = []
    for i in range(len(a)):
        temp = 0
        for j in range(len(b)):
            temp += a[i][j] * b[j][i]
        result.append(temp)
    return result