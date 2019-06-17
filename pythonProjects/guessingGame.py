import random 

random = random.randint(0, 10)

def comp(var1, var2):
    if var1 > var2:
        return 1
    elif var1 < var2:
        return -1
    else:
        return 0 

print('What number do I have between 0 and 10(3 guesses)')

count = 0

while count < 3:
    number = int(input())
    x = comp(random, number)

    if x == 1:
        print("higher than that")
    elif x == -1:
        print("Lower than that")
    else:
        print("well done")

    count += 1
    
