import random

def generateNumber():
    checkList = '0123456789'
    numbers = ''

    while len(numbers) < 3:
        newNumber = random.randint(0, 9)
        newNumber = str(newNumber)
        if newNumber in numbers:
            continue
        else:            
           numbers += newNumber
    
    return str(numbers)

play = 'y'

while play == 'y' or play == 'yes':
    game = generateNumber()
    
    listOf = ''
    
    for i in range(len(game)):
        listOf += game[i]
    guessPlayer = 0
    print(listOf)
    print('''Guess 3 numbers that I have currently stored in my memory
If you have a strike you guessed one out of the 3 numbers and the right spot.
If you have a ball you have guessed one out of the 3 numbers but not the right spot.''')

    while True:
        guessPlayer = input('''Guess...:
''') # ex) 123
        strikes = 0
        balls = 0
        if len(guessPlayer) != 3:
           print('''You did not enter 3 nunbers''')
        else:
            for i in range(len(guessPlayer)):
                for j in range(len(listOf)):
                    if guessPlayer[i] == listOf[j] and i == j:
                        strikes += 1
                    elif guessPlayer[i] == listOf[j] and i != j:
                        balls += 1
                
                
            print('strikes: ' + str(strikes) + ',balls: ' + str(balls))
        if strikes == 3:
            break

    print('yes the secret number is ' + str(listOf) + ' well done')
    play = input('Would you like to play again? (y/n)')
    play = play.lower()
    print (play)
