a = int(input('Please, enter length side a: '))
b = int(input('Please, enter length side b: '))
c = int(input('Please, enter length side c: '))

i = [a, b, c]
P = a + b + c

if a <= 0:
    print('it is impossible to calculate the perimeter')
elif b <= 0:
    print('it is impossible to calculate the perimeter')
elif c <= 0:
    print('it is impossible to calculate the perimeter')
elif a > 0:
    print('P =', P)
elif b > 0:
    print('P =', P)
elif c > 0:
    print('P =', P)

# Не успел найти как сравнивать каждый элемент из списка или перечень переменных с нолём

if 0 < a and 0 < b and 0 < c and P > 20:
    print(max(i))
elif 0 < a and 0 < b and 0 < c and P < 10:
    print(min(i))


