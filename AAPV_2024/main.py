from random import randint

# --- 1. -----------
print('# --- 1. -----------')
a:int = int(input('irja be "a" erteket: '))
b:int = int(input('irja be "b" erteket: '))
if a == 0 or b == 0: print('az eredmeny zero oszto miatt nem hatarozhato meg')
else:
    res = (a+b)/(a*b)
    print (f'[({a}+{b})/({a}*{b})] = {round(res, 2)}')
    if res % 1 == 0: print('egesz szam')
    else: print('valos szam')
print()
# --- 2. -----------
print('# --- 2. -----------')

n:int = randint(1, 100)
print('gondoltam egy szamra, probald meg kitalalni!')
g:int = None
c:int = 0
while g != n:
    g = int(input("tipped: "))
    if g < n: print("tul alacsony!")
    elif g > n: print("tul magas!")
    else: print("eltalaltad!")
    c+=1
print(f'probalkozasaid szama: {c}')
if c > 7: print('legkozelebb gondold at a strategiadat, megy ez jobban is!')
print()
# --- 3. -----------
print('# --- 3. -----------')
class Film:
    def __init__(self, row:str) -> None:
        splts:list[str] = row.strip().split(';')
        self.cim:str = splts[0]
        self.ev:int = int(splts[1])
        self.mufajok:list[str] = splts[2].replace(' ', '').split(',')

filmek:list[Film] = []
file = open('filmek.txt', 'r', encoding='utf-8')
for r in file: filmek.append(Film(r))

print(f'3.1: filmek szama: {len(filmek)}')

c:int = 0
for f in filmek:
    if f.ev >= 2001: c += 1
print(f'3.2: 21. szazadi filmek szama: {c} db')

m:int = 0
for i in range(1, len(filmek)):
    if filmek[i].ev < filmek[m].ev: m = i
print(f'3.3: legkorabbi film: {filmek[m].cim}')

k:str = input(f'3.4 irja be a keresett mufaj nevet:')
lst:list[str] = []
for f in filmek:
    if k in f.mufajok: lst.append(f.cim)
if len(lst) != 0:
    print(f'a {k} mufajmegjelolesu filmek cimei:')
    for c in lst: print(f'\t - {c}')
else: print(f'{k} mufaju film nem talalhato a listan!')
print()