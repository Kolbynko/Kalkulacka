#python kalkulacka
a=str(input('Zadaj priklad: '))

znamienka=[
    a.find('+'),
    a.find('-'),
    a.find('*'),
    a.find('/'),
    ]
def poloha(s, num):
    return int(s[:num]), int(s[num+1:])

if znamienka[0]>0:
    x,y=poloha(a, znamienka[0])
    print(x+y)

if znamienka[1]>0:
    x,y=poloha(a, znamienka[1])
    print(x-y)

if znamienka[2]>0:
    x,y=poloha(a, znamienka[2])
    print(x*y)

if znamienka[3]>0:
    x,y=poloha(a, znamienka[3])
    print(x/y)