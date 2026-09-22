class Pilot:
    def __init__(self, row:str) -> None:
        prts:list[str] = row.strip().split(';')
        self.name:str = prts[0]
        self.nation:str = prts[1]
        self.team:str = prts[2]
        self.qualify:int = int(prts[3])
        self.time:float = float(prts[4])
        self.point:int = int(prts[5])


def get_divisors(num:int) -> list[int]:
    if num < 1: return None
    divisors:list[int] = []
    for x in range(1, (num//2)+1):
        if num % x == 0: divisors.append(x)
    if num != 1: divisors.append(num)
    return divisors


def coprime(x:int, y:int) -> bool:
    common:list[int] = []
    xd = get_divisors(x)
    yd = get_divisors(y)
    for d in xd:
        if d in yd: common.append(d)
    return common == [1]


def first_task() -> None:
    jly:str = input('"j" vagy "ly" van abban a szóban, hogy to_ás?\nválasz: ').lower()
    if jly == 'j': print('helyes!')
    else: print('sajnos nem, úgy írják, hogy "tojás" :(')


def second_task_test() -> None:
    x:int = int(input('kérem az egyik számot: '))
    y:int = int(input('kérem a másik számot: '))
    print(f'{x} osztói: {get_divisors(x)}')
    print(f'{y} osztói: {get_divisors(y)}')
    if coprime(x, y): print(f'{x} és {y} relatív prímek!')
    else: print(f'{x} és {y} NEM relatív prímek!')


def third_task() -> None:
    pilots:list[Pilot] = []
    for r in open('melbourne2009.txt', 'r', encoding='utf8'):
        pilots.append(Pilot(r))
    print(f'1. feladat: célba érkező versenyzők száma: {len(pilots)}')

    sop:int = 0
    for p in pilots:
        sop += p.point
    print(f'2. feladat: kiosztott pontok összesen: {sop}')

    cg:int = 0
    for p in pilots:
        if p.nation == 'germany': cg += 1
    print(f'3. feladat: német versenyzők száma: {cg} fő')

    scrteams:list[str] = []
    for p in pilots:
        if p.point > 0 and p.team not in scrteams:
            scrteams.append(p.team)
    print('4. feladat: pontszerző csapatok:')
    for t in scrteams:
        print(f'\t{t}')

    mti:int = 0
    for i in range(1, len(pilots)):
        if pilots[i].time < pilots[mti].time: mti = i
    print(f'5. feladat: a verseny győztese: {pilots[mti].name} (01:34:{pilots[mti].time})')