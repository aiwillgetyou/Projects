import random
import time

a = 1

while a < 4:
    k = random.randint(0, 10)
    x = random.randint(0, 10)
    y = random.randint(0, 10)
    z = random.randint(0, 10)

    k1 = str(k)
    x1 = str(x)
    y1 = str(y)
    z1 = str(z)

    print('Do you know the answer?')
    formula = k * x + y - z
    print(k1 + '*' + x1 + '+' + y1 + '-' + z1)

    for i in range(1, 4):
        time.sleep(1)
        print(i, end=', ')
        
    answer = int(input())
    if answer == formula:
        print('well done')
        
    else:
        formula = str(formula)
        print('wrong, the answer is ' + formula)
    
    a += 1
