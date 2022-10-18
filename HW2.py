a = int(input('Please, enter length side a: '))
b = int(input('Please, enter length side b: '))
c = int(input('Please, enter length side c: '))

i = [a, b, c]

P = a + b + c

if a == 0:
    print('it is impossible to calculate the perimeter')
elif b == 0:
    print('it is impossible to calculate the perimeter')
elif c == 0:
    print('it is impossible to calculate the perimeter')
elif a > 0:
    print('P =', P)
elif b > 0:
    print('P =', P)
elif c > 0:
    print('P =', P)



if a == 0:
    print('no such triangle exists')
elif b == 0:
    print('no such triangle exists')
elif c == 0:
    print('no such triangle exists')
elif P > 20:
    print(max(i))
elif P < 10:
    print(min(i))
