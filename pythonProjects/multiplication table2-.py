import random

import time


a = 1

while a < 4:

    k = random.randint(0, 10)
    x = random.randint(0, 10)
    k1 = str(k)
    x1 = str(x)

    print('Do you know the answer?')
    formula = k * x
    print(k1 + '*' + x1)

    answer = int(input())
    if answer == formula:
        print('well done')
    else:
        time.sleep(5)
        formula = str(formula)

        print('wrong, the answer is ' +formula)

    
    a += 1
