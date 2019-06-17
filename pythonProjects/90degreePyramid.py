def printLine(n):
    for i in range(number):
        for j in range(1, i + 2):
            if j <= number:
                print(j, end=' ')
        print()

    numberNow = number + 1
    for k in range(number):
        for l in range(1, numberNow):
            if l < numberNow:
                print(l, end=' ')
        numberNow -= 1
        print()


print('give me a number')
number = int(input())
x = printLine(number)
