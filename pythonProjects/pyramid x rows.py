

print('Please enter a number')
row = int(input())
count = 1


while count <= row:
    space = 0
    while space < 2 * (row-count):
        print(' ', end='')
        space += 1
  
    star = 1
    
    while star < 2 * count:
        print('*', end=' ')
        star += 1
        
        
    print()
    count += 1


