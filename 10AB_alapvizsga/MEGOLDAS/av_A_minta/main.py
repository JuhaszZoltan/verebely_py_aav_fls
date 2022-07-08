print('-----A-----')


# 1. feladat
szvg = input('írjon be egy legalább 9 karakterből álló szöveget: ')
if len(szvg) > 8:
    szvg = szvg.lower()
    for i in range(len(szvg)):
        print(szvg[len(szvg) - 1 - i], end='')
else:
    print(f'a(z) {szvg} kevesebb, mint 9 karakter hosszú!')


# 2. feladat
print('''
paradicsom:  1199 Ft/Kg
paprika:     1349 Ft/Kg
vöröshagyma:  289 Ft/Kg
''')
sum = 0
while True:
    vlsz = input('kíván valamit vásárolni? ').lower()
    if vlsz == 'nem': break
    trmk = input('\tmelyik termékből? ').lower()
    p = 0
    if trmk == 'paradicsom': p = 1199
    elif trmk == 'paprika': p = 1349
    elif trmk == 'vöröshagyma': p = 289
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
        self.fazis = v[1]
        self.premier:str = v[2]
        self.koltseg = int(v[3])
        self.bevetel = int(v[4])

filmek:list[Film] = []
for r in open("../marvel.txt", encoding='utf-8'):
    filmek.append(Film(r))

print(f"3.1: {len(filmek)} filmje van a marvel moziverzumának")

sk = 0
for f in filmek: sk += f.koltseg
print(f'3.2: a filmek átlagos gyártási költsége: ${round(sk/len(filmek), 2)}M')

mi = 0
for i in range(1, len(filmek)):
    if filmek[i].bevetel / filmek[i].koltseg > filmek[mi].bevetel / filmek[mi].koltseg: mi = i
print(f'3.3: a legköltséghatékonyabb film címe: {filmek[mi].cim}')

y:str = input('3.4: írjon be egy évszámot: ')
print(f'a {y}-ban/ben megjelent marvel filmek:')
for f in filmek:
    if(y in f.premier): print(f'  {f.cim}')

