

# for loop
for x in range(2, 9+1):
    for y in range(1, 9+1):
        print(x, ' * ', y, ' = ', x*y)
        # print(str(x) + ' * ' + str(y) + ' = ' + str(x*y))
        # print('%d * %d = %d' % (x, y, x*y))

# while loop
x = 2
while x < 9+1:
    y = 1
    while y < 9+1:
        print(x, ' * ', y, ' = ', x*y)
        # print(str(x) + ' * ' + str(y) + ' = ' + str(x*y))
        # print('%d * %d = %d' % (x, y, x*y))
        y += 1
    x += 1

# while loop + table
x = 2
s1="\t"
for i in range(1, 9+1):
    s1 = s1 + str(i) + '\t'
print(s1)
while x < 9+1:
    y = 1
    s2='*' + str(x) + '=\t'
    while y < 9+1:
        s2 = s2 + str(x*y) + '\t'
        y += 1
    print(s2)
    x += 1