import random


play = 'yes'


while play == 'yes' or play == 'y':

    randomNumber = random.randint(0, 2)

    if randomNumber == 0:
        computer = 'rock'
    elif randomNumber == 1:
        computer = 'paper'
    else:
        computer = 'scissor'

    user = input('rock? paper? scissor?:')

    if user == 'rock':
        if computer == 'rock':
            print("it's a tie")
        elif computer == 'scissor':
            print("The computer chose %s you chose %s" % (computer, user))
            print("You Win!")
        else:
            print("The computer chose %s you chose %s" % (computer, user))
            print("You Lose:(")

    if user == 'paper':
        if computer == 'paper':
            print("it's a tie")
        elif computer == 'rock':
            print("The computer chose %s you chose %s" % (computer, user))
            print("You Win!")
        else:
            print("The computer chose %s you chose %s" % (computer, user))
            print("You Lose")

    if user == 'scissor':
        if computer == 'scissor':
            print("it's a tie")
        elif computer == 'paper':
            print("The computer chose %s you chose %s" % (computer, user))
            print("You Win!")
        else:
            print("The computer chose %s you chose %s" % (computer, user))
            print("You Lose")

    play = input("would you like to play again? yes/or :")
