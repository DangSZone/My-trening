def get_matrix(n, m, value):
    matrix = list()
    for j in range(n, n+1):
        k = []
        for i in range(m, m+1):
            k = [value] * i
            matrix = [k] * j
        return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
result4 =  get_matrix(46,2,188)
res5 = get_matrix(0,2,6)
print(result1)
print(result2)
print(result3)
print(result4)
print(res5)













