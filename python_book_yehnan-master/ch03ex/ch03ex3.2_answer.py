

def f(n):
    if n < 0:
        n = 0
    elif n > 255:
        n = 255
        
    if 0 <= n <= 130:
        a0, a1 = 0, 130
        b0, b1 = 0, 60
    elif 130 < n < 200:
        a0, a1 = 130, 200
        b0, b1 = 60, 85
    else: # 200 <= n <= 255
        a0, a1 = 200, 255
        b0, b1 = 85, 100
        
    return int((n - a0) / (a1 - a0) * (b1 - b0) + b0)


if __name__ == '__main__':
    # simple tests
    if f(0) != 0:
        print('Failed')
    if f(130) != 60:
        print('Failed')
    if f(200) != 85:
        print('Failed')
    if f(255) != 100:
        print('Failed')

print("f(0): %d" % f(0))
print("f(130): %d" % f(130))
print("f(180): %d" % f(180))
print("f(200): %d" % f(200))
print("f(225): %d" % f(225))
print("f(255): %d" % f(255))
print("f(2553): %d" % f(2553))
print("f(-3): %d" % f(-3))

