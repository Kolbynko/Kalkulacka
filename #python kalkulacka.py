#python kalkulacka
a=str('13+3+6')
a=a.strip()
#pozicia znamienka == pos
pos=0

znamienka=[]
cisla=[]

for i in range (0, int(len(a))):
    if a[i] in '+-*/'== True:
        znamienka.append(a[])
        cisla.append(a[pos:i])
        pos=i+1
cisla.append(a[pos:])
print(cisla)
print(znamienka)
