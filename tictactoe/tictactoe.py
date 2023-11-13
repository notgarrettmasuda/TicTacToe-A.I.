"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xCount = 0
    yCount = 0
    for row in board:
        for symbol in row:
            if symbol == X:
                xCount += 1
            elif symbol == O:
                yCount +=1
    if xCount > yCount:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == EMPTY:
                actions.add((x, y))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    boardCopy = []
    for row in board:
        boardCopy.append(row.copy())

    symbol = player(board)
    try:
        boardCopy[int(action[0])][int(action[1])] = symbol
        return boardCopy
    except:
        print("action is outside the range of the board")
        return board


def rowWin(board, symbol):
    for x in range(len(board)):
        count = 0
        for y in range(len(board)):
            if board[x][y] == symbol:
                count += 1
                if count >= 3:
                    return True
            else:
                count = 0
    return False

def columnWin(board, symbol):
    for x in range(len(board)):
        count = 0
        for y in range(len(board)):
            if board[y][x] == symbol:
                count += 1
                if count >= 3:
                    return True
            else:
                count = 0
    return False

def diagonalWin(board, symbol):
    if board[1][1] == symbol:
        if (board[0][0] == symbol and board[2][2] == symbol) or (board[0][2] == symbol and board[2][0] == symbol):
            return True
    else:
        return False


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if rowWin(board, X) or columnWin(board, X) or diagonalWin(board, X):
        return X
    elif rowWin(board, O) or columnWin(board, O) or diagonalWin(board, O):
        return O
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    count = 0
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] != None:
                count += 1
    if count == 9:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if rowWin(board, X) or columnWin(board, X) or diagonalWin(board, X):
        return 1
    elif rowWin(board, O) or columnWin(board, O) or diagonalWin(board, O):
        return -1
    else:
        return 0

def maxValue(board):
    #returns best move possible for X
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, minValue(result(board, action)))
    return v

def minValue(board):
    #returns best move possible for O
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, maxValue(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board) == X:
        plays = []
        for action in actions(board):
            plays.append([minValue(result(board, action)), action])
        return sorted(plays, key=lambda x: x[0], reverse = True)[0][1]
    elif player(board) == O:
        plays = []
        for action in actions(board):
            plays.append([maxValue(result(board, action)), action])
        return sorted(plays, key=lambda x: x[0])[0][1]