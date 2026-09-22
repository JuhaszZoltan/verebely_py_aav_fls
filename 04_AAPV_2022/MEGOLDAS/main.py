# 1. feladat:
print('\n1. feladat:')
karakterlanc:str = input('írjon be egy tetszőleges szöveget: ').lower()
szam:int = int(input('Írjon be egy pozitív egész számot: '))
print(szam * f'{karakterlanc} ')

# 2. feladat:
print('\n2. feladat:')
print('adja meg a másodfokú egyenlet együtthatóit!')
print('[ax^2 + bx + c = 0]')
a:float = float(input('a = '))
b:float = float(input('b = '))
c:float = float(input('c = '))
if a == 0:
    print('az egyenlet nem másodfokú')
else:
    d:float = pow(b, 2) - 4 * a * c
    if d < 0:
        print('az egyenletnek nincs valós megoldása')
    elif d == 0:
        print('az egyenletnek csak egy valós megoldása van:')
        print(f'x = {-b / (2 * a)}')
    else:
        print('az egyenletnek két valós megoldása van:')
        print(f'xˇ1 = {(-b + d) / (2 * a)}')
        print(f'xˇ2 = {(-b - d) / (2 * a)}')

# 3. feladat:
print('\n3. feladat:')

class Bolygo:
    def __init__(self, sor:str):
        s:list[str] = sor.strip().split(';')
        self.nev:str = s[0]
        self.holdak_szama:int = int(s[1])
        self.terfogat_arany:float = float(s[2])


bolygok:list[Bolygo] = []
for sor in open('solsys.txt', encoding='UTF-8'):
    bolygok.append(Bolygo(sor))
print(f'3.1: bolygók száma a naprendszerben: {len(bolygok)} db')

osszes_hold:int = 0
for bolygo in bolygok:
    osszes_hold += bolygo.holdak_szama
print(f'3.2: holdak száma a naprendszerben: {osszes_hold} db')

mini = 0
for i in range(1, len(bolygok)):
    if bolygok[i].terfogat_arany < bolygok[mini].terfogat_arany:
        mini = i
print(f'3.3: a legkisebb térfogatú bolygó: {bolygok[mini].nev}')

keresett_bolygo:str = input('3.4: írd be a keresett bolygó nevét: ')
for bolygo in bolygok:
    if bolygo.nev.lower() == keresett_bolygo.lower():
        print(f'van {keresett_bolygo} nevű bolygó a naprendszerben')
        break
else: print(f'nincs {keresett_bolygo} nevű bolygó a naprendszerben')