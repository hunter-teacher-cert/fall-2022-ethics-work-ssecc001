# FILENAME gol.py
# First Last Susie Seccafico
# CSCI 77800 Fall 2022
# collaborators: Stacy Goldstein
# consulted: summer work and python sources 
import random

def createCharArray(count):
    b = []
    for i in range(count):
        b.append('-')

    return b

def createNewBoard(rows, cols):
    board = []
    for i in range(rows):
        board.append(createCharArray(cols))

    return board

def printBoard(board):
    for b in board:
        for x in b:
            print(x, end="")
        print("")

def setCell(board, r, c, val):
    board[r][c] = val

def createRandomBoard(rows, columns):
    board = []
    for i in range(rows):
        b = createCharArray(columns)
        for j in range(columns):
            b[j] = '-' if random.randint(0, 3) < 2 else 'X'

        board.append(b)

    return board

# return number of living neigbours of board[r][c]
def countNeighbours(board, r, c):
    row = len(board)
    col = len(board[0])

    count = 0

    for i in range(max(0, r - 1), min(row, r + 2)):        
        for j in range(max(0, c - 1), min(col, c + 2)):
            if not (i == r and j == c):
                if board[i][j] != '-':
                    count += 1

    return count
        
def getNextGenCell(board, r, c):
    liveNeighbors = countNeighbours(board, r, c)

    if board[r][c] == 'X': # if cell is alive
        if liveNeighbors == 2 or liveNeighbors == 3: # and has 2 or 3 neighboors
            return 'X'
    else: # if cell is dead
        if liveNeighbors == 3: # and has exactly 3 neighbors
            return 'X'
