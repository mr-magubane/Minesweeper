from difflib import diff_bytes
import random

EASY_DIFF = 0.15
MEDIUM_DIFF = 0.20
HARD_DIFF = 0.25

SMALL_SIZE = 9
MEDIUM_SIZE = 12
LARGE_SIZE = 15

def startGame():

    game = createGame()

def createGame():
    '''Creates the size and difficulty of the game by returning an array'''

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

    '''2x2 array, each block has 2 values: [Boolean, int]

    boolean: If True the block has not been selected yet
    int: None(blank), 0(mine), int > 1(number of surrounding mines)'''

    #Create blank mineField
    mineField = []
    for row in range(gameSize):
        mineField.append([])
        for value in range(gameSize):
            mineField[row].append([True, None])
    ans = add_numbers(add_mines(gameSize, difficulty, mineField))

    for x in ans:
        for y in range(9):
            print(x[y][1], end='   ')
        print('\n')

def add_mines(size, diff, field):
    
    number_of_mines = int((size**2)*diff)

    while number_of_mines > 0:
        row = random.randrange(0,(size-1))
        column = random.randrange(0,(size-1))

        if field[row][column][1] == 0:
            continue
        field[row][column][1] = 0
        number_of_mines -= 1
    return field

def add_numbers(field):

    for row in range(len(field)):

        for column in range(len(field)):

            mines_around = 0
            if field[row][column][1] == 0:
                continue
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    try:
                        if field[row+x][column+y][1] != 0:
                            continue
                    except:
                        continue
                    mines_around += 1
            field[row][column][1] = mines_around
    return field

# startGame()

createGame()