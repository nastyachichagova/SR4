x=float(input('Введите длину первого катета: '))
y=float(input('Введите длину второго катета: '))
if ((x>0) and (y>0)):
    S = x*y/2
    P = x+y+(x**2+y**2)**(1/2)
    print ('S = ', S)
    print ('P = ', P)
else:
    print ('Ошибка!')
