from operator import index

i= int(input())
def key(i):
    result = []
    result1 = []
    for j in range(1,20):
        for k in range(2,20):
            if j>i or j==i:
                break
            sum = j+k
            if i % sum == 0 and j != k:
                result1.append([j,k])
                for o in result1:
                    o.sort()
                if result1.count([j,k]) == 1 and [j,k] not in result:
                    result.extend([j,k])
                else:
                    continue
            elif i < j+k:
                break
    result = ''.join(str(l) for l in result)
    return result

res = int(key(i))
print(res)

import module_Test
ok = False
m = module_Test.meme
for e in m:
    if res == e:
        ok = True
        print(True)
    if ok == True:
        break
    elif index(e) != 16:
        continue
    else:
        print("end")