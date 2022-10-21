a = int(input('Please, enter length side a: '))
b = int(input('Please, enter length side b: '))
c = int(input('Please, enter length side c: '))

i = [a, b, c]

if a <= 0:
    print('no such triangle exists')
elif b <= 0:
    print('no such triangle exists')
elif c <= 0:
    print('no such triangle exists')
elif (a + b + c) > 20:
    print('P =', a + b + c)
    print(max(i))
elif (a + b + c) < 10:
    print('P =', a + b + c)
    print(min(i))