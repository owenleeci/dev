

def group(iterable, size):
    result = []
    li = list(iterable)    # 轉成list
    length = len(li)
    for i in range(0, length, size):  # range(start, stop[, step]), [0, 3, 6]
        result.append(li[i:i+size])   # li[0:3], li[3:6], li[6:9]
    return result

print(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
# [[1, 2, 3, 4], [5, 6, 7, 8], [9]]

print(group(range(20), 5))
# [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]

print(group(range(1, 24, 2), 5))
# [[1, 3, 5, 7, 9], [11, 13, 15, 17, 19], [21, 23]]
