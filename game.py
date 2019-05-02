word = input('Please enter world:  ')


def hangman(word):
    wrong = 0
    stages = ["",
              " _ _ _ _   ",
              "|     |     ",
              "|     O     ",
              "|    /|\    ",
              "|    / \    ",
              "| you  lose "]
    rletters = list(word)
    board = ['_'] * len(word)
    win = False
    print('Hello Hall')
    while wrong < len(stages) - 1:
        print('\n')
        char = input('Enter letter:  ')
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((' '.join(board)))
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print('WINNER')
            print(' '.join(board))
            win = True
            break

hangman(word)
