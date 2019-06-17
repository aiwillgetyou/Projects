def add(plus, cal):
    resultAdd = float(cal) + float(plus)
    return resultAdd

def sub(sub, cal):
    resultSub = float(cal) - float(sub)
    return resultSub

def mul(mul, cal):
    resultMul = float(cal) * float(mul)
    return resultMul

def div(div, cal):
    resultDiv = float(cal) / float(div)
    return resultDiv
    


mainCalc = float(0)

addOn = float(0)
subFrom = float(0)
mulWith = float(0)
DivWith = float(0)
exitNow = ''

print('first operand is 0')

while exitNow == '':
    operator = input('''Choose an operator: +, -, /, * or exit ''')

    if operator == '+':
        addOn = input('enter number: ')
        mainCalc = add(addOn, mainCalc)
        print(mainCalc)
        
    elif operator == '-':
        subFrom = input('enter number: ')
        mainCalc = sub(subFrom, mainCalc)
        print(mainCalc)

    elif operator == '*':
        mulWith = input('enter number: ')
        mainCalc = mul(mulWith, mainCalc)
        print(mainCalc)

    elif operator == '/':
        divWith = input('enter Number: ' )
        mainCalc = div(divWith, mainCalc)
        print(mainCalc)

    elif operator == 'exit':
        break

    else:
        print('wrong input')
        
    
        
        
    
