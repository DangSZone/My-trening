i= int(input())
def key(i):
    result = []
    for j in range(1,20):
        for k in range(2,20):
            if j>i or j==i:
                break
            sum = j+k
            if i % sum == 0 and j != k:
                if j and k not in result:
                    result.extend([j, k])
                else:
                    break
            elif i < j+k:
                break
    return result
    result.clear()
res = key(i)
print(*res)
