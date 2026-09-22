print('-----B-----')


# 1. feladat
szvg = input('írjon be egy legfeljebb 11 karakterből álló szöveget: ')
if len(szvg) < 12:
    szvg = szvg.upper()
    for i in range(len(szvg)):
        print(szvg[len(szvg) - 1 - i], end='')
else:
    print(f'a(z) {szvg} több, mint 11 karakter hosszú!')


# 2. feladat
print('''
banán:        569 Ft/Kg
szőlő:       1698 Ft/Kg
görögdinnye:  499 Ft/Kg
''')
sum = 0
while True:
    vlsz = input('kíván valamit vásárolni? ').lower()
    if vlsz == 'nem': break
    trmk = input('\tmelyik termékből? ').lower()
    p = 0
    if trmk == 'banán': p = 569
    elif trmk == 'szőlő': p = 1698
    elif trmk == 'görögdinnye': p = 499
    else:
        print('\tnincs ilyen termék!')
        continue
    h = float(input(f'\thány Kg {trmk}(o)t szeretne? '))
    sum += (p * h)
print('köszönjük a vásárlást!')
print(f'fizetendő összeg: {round(sum)}Ft')


# 3. feladat
class Film:
    def __init__(self, r:str):
        v = r.strip().split(';')
        self.cim = v[0]
        self.fazis:int = int(v[1])
        self.premier:str = v[2]
        self.koltseg = int(v[3])
        self.bevetel = int(v[4])

filmek:list[Film] = []
for r in open("../marvel.txt", encoding='utf-8'):
    filmek.append(Film(r))

print(f"3.1: {len(filmek)} filmje van a marvel moziverzumának")

fb3c = 0
for f in filmek:
    if f.fazis < 3: fb3c += 1
print(f'3.2: a 3. fázis előtti filmek száma: {fb3c}db')

mi = 0
for i in range(1, len(filmek)):
    if filmek[i].bevetel - filmek[i].koltseg < filmek[mi].bevetel - filmek[mi].koltseg: mi = i
print(f'3.3: a legalacsonyabb hasznot a(z): {filmek[mi].cim} c. film hozta')

cp:str = input('3.4: írjon be egy címrészletet: ').lower()
print(f'Az alábbi filmek címében szerepel ez a kifejezés:')
for f in filmek:
    if(cp in f.cim.lower()): print(f'  {f.cim}')

