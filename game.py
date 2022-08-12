import random

EASY_DIFF = 0.15
MEDIUM_DIFF = 0.20
HARD_DIFF = 0.25

SMALL_SIZE = 9
MEDIUM_SIZE = 12
LARGE_SIZE = 15

def startGame():

    difficulty = gameSettings()[0]
    size = gameSettings()[1]

    mineField = createGame(size)
    mineField = add_mines(difficulty, size, mineField)
    mineField = add_numbers(mineField)

    showField (mineField)

    # while not isGameOver():
    #     ask_player_for_move
    #     updateField
    #     showField(updateField)
def gameSettings():
    '''Creates the size and difficulty of the game by returning an array with all None values'''

    difficulty = 'easy' #input("Choose Game Difficulty:\neasy\nmedium\nhard\n--> ") 
    while True:
        if difficulty == 'easy':
            difficulty = EASY_DIFF
            break
        elif difficulty == 'medium':
            difficulty = MEDIUM_DIFF
            break
        elif difficulty == 'hard':
            difficulty = HARD_DIFF
            break
        else:
            difficulty = input('Please choose correct difficulty (easy, medium or hard) \n--> ')

    gameSize = 'small' #input("Choose Game Size:\nsmall\nmedium\nlarge\n--> ")
    while True:
        if gameSize == 'small':
            gameSize = SMALL_SIZE
            break
        elif gameSize == 'medium':
            gameSize = MEDIUM_SIZE
            break
        elif gameSize == 'large':
            gameSize = LARGE_SIZE
            break
        else:
            difficulty = input('Please choose correct Game Size (9 x 9, 12 x 12 or 15 x 15) \n--> ')
    return (difficulty, gameSize)

def createGame(gameSize):

    '''2x2 array, each block has 2 values: [Boolean, int]

    boolean: If True the block has not been selected yet
    int: None(blank), 0(mine), int > 1(number of surrounding mines)'''

    #Create blank mineField
    mineField = []
    for row in range(gameSize):
        mineField.append([])
        for value in range(gameSize):

            mineField[row].append([True, ' '])
    
    return mineField

def add_mines(diff, size, field):

    number_of_mines = (diff*(size**2))

    while number_of_mines > 0:
        row = random.randrange(0,(size-1))
        column = random.randrange(0,(size-1))

        if field[row][column][1] == '*':
            continue
        field[row][column][1] = '*' 
        number_of_mines -= 1
    
    return field

def add_numbers(field):

    for row in range(len(field)):

        for column in range(len(field)):

            mines_around = 0
            if field[row][column][1] == '*':
                continue
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    try:
                        if field[row+x][column+y][1] != '*':        #Update except condition
                            continue
                    except:
                        continue
                    mines_around += 1
            field[row][column][1] = mines_around
            if mines_around == 0:
                field[row][column][1] = ' '
    return field

def showField (field):
    row_count = 0
    print('    ', end='')
    for column in range(len(field)):
        print('   {}'.format(column+1), end='')
    print('\n')
    for row in field:
        row_count += 1
        print('{}    | '.format(row_count), end='')
        for column in range(len(field)):
            if row[column][0] == False:
                print('?', end=' | ')
            else:
                print(row[column][1], end=' | ')
        print('\n')

def make_a_move():
    reply = 'n'
    while reply != 'y':
        print('MAKE A MOVE')
        row = input('Select the row: ')
        if int(row) not in range(1,10):                                #Add try except
            continue
        column = input('Select the column: ')
        if int(column) not in range(1,10):                                #Add try except
            continue
        print('Is This Your Move?(y/n)  ->', 'Row:', row, 'Column:', column)
        reply = input()
    return (row, column)


startGame()
make_a_move()
