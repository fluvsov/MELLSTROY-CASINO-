import random

казик = ["чекушка","жирность","бурмалда"]

def казино():
    b1 = random.choice(казик)
    b2 = random.choice(казик)
    b3 = random.choice(казик)
    print(f"\033[32m{b1} {b2} {b3}\033[0m")
    if b1 == b2 == b3:
        print("\033[33mДЖЕКПОТ\033[0m")

print("""\033[36mКАЗИНО МЕЛЛСТРОЙНОСТИ by fluvsov
напишите <казино()> для запуска\033[0m""")
