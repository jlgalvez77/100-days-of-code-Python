import random

game_images = [rock, paper, scissors]

player = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n'))
if player >= 3 or player < 0:
    print('Wrong option')
else:
    print(game_images[player])

    computer = random.randint(0, 2)
    print('Computer chose:')
    print(game_images[computer])

    if player == 0 and computer == 2:
        print('You win!!')
    elif computer == 0 and player == 2:
        print('You lose')
    elif computer > player:
        print('You lose')
    elif player > computer:
        print('You win')
    elif computer == player:
        print('It is a draw')
