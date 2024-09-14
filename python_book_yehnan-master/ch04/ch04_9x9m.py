def group(iterable, size):
    result = []
    li = list(iterable)    # 轉成list
    length = len(li)
    for i in range(0, length, size):  # range(start, stop[, step]), [0, 3, 6]
        result.append(li[i:i+size])   # li[0:3], li[3:6], li[6:9]
    return result

result = []
for x in range(2, 9+1):
    for y in range(1, 9+1):
        result.append(str(x) + '*' + str(y) + '=' + str(x*y))

print(result)

####

result = [str(x)+'*'+str(y)+'='+str(x*y) for x in range(2, 9+1) 
                                         for y in range(1, 9+1)]

print(result)

result = [x*y for x in range(2, 9+1) 
               for y in range(1, 9+1)]

g = group(result, 9)
for l in g:
    print(l)
