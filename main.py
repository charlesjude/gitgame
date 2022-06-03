import random
while True:
    choices = ['r', 'p', 's']
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input('pls enter any the 3 letter, r, p, s:')
        print('its an error')
    if player == computer:
        print('you both tie!')
    elif player == 'r':
        if computer == 's':
            print('you win')
        elif player == 'p':
            if computer == 'r':
                print('you lose')
        elif player == 's':
            if computer == 'p':
                print('you win')

                replay = input('play against? (yes/no)')
            if replay != 'yes':
                    break
                    print('good bye')



