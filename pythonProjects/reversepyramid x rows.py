print('how many levels pyramid')

rows = int(input())

reverseRow = rows
countReverse = 0

while reverseRow > 1:
    
    
    
    spaceReverse = 0
    while spaceReverse < 2 * countReverse:
        print(' ', end='')
        spaceReverse += 1


    starReverse = 0
    while starReverse < 2 * reverseRow - 1:
        print('*', end=' ')
        starReverse += 1

    reverseRow -= 1
    countReverse += 1
    print()
    

countPyramid = 0

while countPyramid < rows:


    countPyramid += 1
    spacesPyramid = 0

    while spacesPyramid < 2 * (rows - countPyramid):
        print(' ', end= '')
        spacesPyramid += 1

    starsPyramid = 1
    while starsPyramid < 2 * countPyramid:
        print('*', end= ' ')
        starsPyramid += 1

    print() 

