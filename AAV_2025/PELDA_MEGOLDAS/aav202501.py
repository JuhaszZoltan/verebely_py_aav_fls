from random import choice

FILE_PATH:str = 'FELADAT\\nascar.txt'
MI_TO_KM:float = 1.609344
DRIVER_NAME:str = 'Jimmie Johnson'

feladvanyok:list[str] = [
    "narancs",
    "elefánt",
    "budapest",
    "tanár",
    "kosárlabda",
    "napraforgó",
    "bíbor",
    "helikopter",
    "palacsinta",
    "zongora"
]

class Season:
    def __init__(self, row:str) -> None:
        tmp:list[str] = row.strip().split(';')
        self.year:int = int(tmp[0])
        self.races:int = int(tmp[1])
        self.driver:str = tmp[2]
        self.manufacturer:str = tmp[3]

def get_puzzle(obj:str, tps:list[str]) -> str:
    pzzl:str = ''
    for c in obj.lower():
        if c == ' ': pzzl += ' '
        elif c in tps: pzzl += c
        else: pzzl += '_'
    return pzzl

def is_tip_correct(npt:str, tps:list[str]) -> bool:
    if not npt.isalpha():
        print('csak betű lehet a tipp!')
        return False
    if len(npt) != 1:
        print('csak egyetlen karakter lehet a tipp!')
        return False
    if npt in tps:
        print('ez a betűt már egyszer tippelted!')
        return False
    return True

def f1() -> None:
    mi:float = float(input('írja be hogy hány mérföldet szeretne átváltani: '))
    print(f'{mi} mérföld {mi * MI_TO_KM:.3f} km')

def f2() -> None:
    objective:str = choice(feladvanyok)
    tips:list[str] = []
    puzzle:str = get_puzzle(objective, tips)
    mistakes:int = 0
    while objective != puzzle and mistakes != 13:
        print(f'feladvány: {puzzle}')
        if len(tips) > 0:
            tips_str = ', '.join(tips)
            print(f'eddig tippelt betűk: {tips_str}')
        print(f'hibapontok: {mistakes}')
        char:str = input('írj be egy betűt: ').lower()
        if is_tip_correct(char, tips):
            tips.append(char)
            tips.sort()
            if char not in objective: mistakes += 1
            else: puzzle = get_puzzle(objective, tips)
        print('-----------')
    print(f'hibapontok száma: {mistakes}')
    print(f'megoldás: {objective}')
    if objective == puzzle: print('NYERTÉL!')
    else: print('VESZTETTÉL!')

def f3() -> None:
    seasons:list[Season] = []
    stream = open(FILE_PATH)
    for r in stream: seasons.append(Season(r))
    
    print(f'#3.1: évadok száma: {len(seasons)}')

    m:int = 0
    for i in range(1, len(seasons)):
        if seasons[i].races > seasons[m].races: m = i
    print(f'#3.2: az {seasons[m].year}es szezonban rendezték a legtöbb versenyt')

    years:list[str] = []
    for s in seasons:
        if s.driver == DRIVER_NAME: years.append(f'{s.year}')
    print(f'#3.3: {DRIVER_NAME} a következő években lett bajnok:')
    print(f'\t{", ".join(years)}')

    name:str = input('#3.4: írja be a versenyző nevét: ')
    cups:int = 0
    for s in seasons:
        if s.driver == name:
            cups += 1
    if cups == 0: print(f'\tnem volt {name} nevű bajnok a NASCAR történelmében')
    else: print(f'\t{name} összesen {cups} alkalommal volt bajnok')

    manufacturers:list[str] = []
    for s in seasons:
        if s.manufacturer not in manufacturers and s.manufacturer not in {'not awarded', 'Chevrolet'}:
            manufacturers.append(s.manufacturer)
    manufacturers.sort()
    print('#3.5: a következő gyártók nyertek még bajnokságot:')
    for m in manufacturers: print(f'\t- {m}')

print('------------------')
f1()
print('------------------')
f2()
print('------------------')
f3()