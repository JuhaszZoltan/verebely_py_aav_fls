def feladat_1() -> None:
    print('1. feladat:')
    x:int = int(input('kérem a hatványalapot: '))
    n:int = int(input('kérem a sorozat hosszát: '))
    print(f'{x} első {n} hatványa:')
    for k in range(n):
        print(f'{pow(x, k+1)}', end=' ')
    print()


def feladat_2() -> None:
    print('2. feladat:')
    print('''árlista
----------------------
|pesszó kávé:    80Ft|
|hosszú kávé:    90Ft|
|cappuchino:    100Ft|
|extra cukor:   +10Ft|
|saját pohárba: -15Ft|
----------------------''')
    f:str = input('milyen kávét szeretnél? ')
    c:bool = True if input('kérsz bele extra cukrot (I/N)? ') == "I" else False
    p:bool = True if input('van saját poharad (I/N)? ') == "I" else False
    if str.startswith(f, 'presszó'): ar = 80
    elif str.startswith(f, 'hosszú'): ar = 90
    elif str.startswith(f, 'cappuchino'): ar = 100
    if c: ar += 10
    if p: ar -= 15
    print(f'a kávéd {ar}Ft-ba kerül!')


class Termek:
    def __init__(self, sor:str):
        v:list[str] = sor.strip().split(';')
        self.kod:str = v[0]
        self.nev:str = v[1]
        nev_reszek:list[str] = self.nev.split(' ')
        self.kiszereles_mennyiseg:int = int(nev_reszek[-2].strip('('))
        self.kiszereles_mertekegyseg:str = nev_reszek[-1].strip(')')
        self.ar:int = int(v[2])
        self.db:int = int(v[3])


def get_kinalat() -> list[Termek]:
    termekek:list[Termek] = []
    for sor in open('vm.txt', encoding='utf-8'):
        termekek.append(Termek(sor))
    return termekek


def feladat_3_3(lst:list[Termek]) -> None:
    print(f'f3.3: az automatában {len(lst)} különböző termék van')


def feladat_3_4(lst:list[Termek]) -> None:
    mini = 0
    for i in range(1, len(lst)):
        if lst[i].ar < lst[mini].ar: mini = i
    print(f'f3.4: a legolcsóbb termék a(z) {lst[mini].nev} ({lst[mini].ar}Ft)')


def feladat_3_5(lst:list[Termek]) -> None:
    s:int = 0
    for t in lst:
        if t.kiszereles_mertekegyseg == 'ml':
            s += t.kiszereles_mennyiseg*t.db
    print(f'f3.5: összesen {s/1000} liter üdítőital van még az automatában')


def feladat_3_6(lst:list[Termek]) -> None:
    s:int = 0
    for t in lst:
        s += t.ar*(12-t.db)
    print(f'f3.6: összesen {s}Ft van az automatában')