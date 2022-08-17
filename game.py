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
    updateField(mineField, ask_for_move(size))

    # while not isGameOver():
    #     move = ask_for_move(size)
    #     mineField = updateField(mineField, move)
    #     showField(updateField)
def gameSettings():



    '''asks user for the game difficulty and size of the field'''

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
    '''Adds mines to the minefield'''
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
    '''Adds the numbers to the minefield'''
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
    '''prints out the current field'''
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

def ask_for_move(size):
    '''Asks player for a move and returns the the row(int) and column(int) '''
    reply = 'n'
    while reply != 'y':
        print('MAKE A MOVE')
        print("Select the row from 1 to ", size,":", end="")
        row = input()
        if int(row) not in range(1,10):
            print("Invalid input Try again!\n")                                
            continue
        print("Select the column from 1 to ", size,":", end="")
        column = input()
        if int(column) not in range(1,10):  
            print("Invalid input Try again!\n")                                
            continue
        print('Is This Your Move?(y/n)  ->', 'Row:', row, 'Column:', column)
        reply = input()
        if reply != 'y' and reply != 'n':
            print("Invalid input Try again!\n")                                
            continue
    return [int(row), int(column)]

def updateField (mineField, move):
    '''Updates the field, based on the players move'''
    print('move =', move[0], move[1])
    block_chosen = mineField[move[0]-1][move[1]-1][1]
    hidden = mineField[move[0]][move[1]][0] 

    if block_chosen == '*':
        print('Game Over!\n ---You Lose!---')
        exit()
    if block_chosen == ' ':
        print('blank')
    else:
        print('this a number', block_chosen )
    

startGame()
#Index out of range when move row or column is 9