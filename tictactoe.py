"""
Tic Tac Toe Player
"""

import math
import copy

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
    if board == initial_state():
        return X
    
    x_count = 0
    o_count = 0
    for row in board:
        x_count += row.count(X)
        o_count += row.count(O)

    if x_count == o_count:
        return X
    else:
        return O




def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for i in range (3):
        for j in range (3):
            if board[i][j] == EMPTY:
                possible_actions.add((i,j))
    if len(possible_actions) == 0:
        return 0
    else:
        return possible_actions




def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    new_board = copy.deepcopy(board)
    try: 
        if new_board[[action[0]][action[1]]] == EMPTY:
            new_board[[action[0]][action[1]]] = player(new_board)
        else: 
            raise Exception
    except Exception:
        print("Non-valid action: Spot occupied")
        
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
    # check columnss
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            return board[0][j]
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]    
    elif board[2][0] == board[1][1] == board[0][2]:
        return board[2][0]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O or actions(board) == 0:
        return True
    else: 
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (winner(board)) == X:
        return 1
    elif (winner(board)) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    else:
        best_move = None
        if player(board) == X:
            value, best_move = maxvalue(board)
        else: 
            value, best_move = minvalue(board)
        return best_move

def maxvalue(board): # based on pseudo code
    """
    Returns the max value and best move of maximising player
    """
    v = float("-inf")
    move = None
    if terminal(board):
        return utility(board)
    for action in actions(board):
        outcome_value, act = minvalue(result(board,action))
        if outcome_value > v:
            v = outcome_value
            move = action
            if v == 1:
                return v, move
    return v, move

def minvalue(board): # based on pseudo code
    """
    Returns the min value and best move of minimizing player
    """
    v = float("-inf")
    move = None
    if terminal(board):
        return utility(board)
    for action in actions(board):
        outcome_value, act = maxvalue(result(board,action))
        if outcome_value < v:
            v = outcome_value
            move = action
            if v == 1:
                return v, move
    return v, move
