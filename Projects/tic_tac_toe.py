'''
TIC TAC TOE - A SIMPLE 2-PLAYERS GAME

Steps:

0- The players decide who is Player1 and Player2
1- The game randomizes what Player goes first
2- The first Player chooses a Mark: X or O
--REPEAT--
3- The Player chooses a position for his/hers next Mark
4- The game checks if Victory or Full_Board
5- If Victory, the game informs what Player won and asks if Replay (else:REPEAT)
6- If Full_Board, the game informs draw and asks if Replay (else:REPEAT)
--REPEAT
7- If Replay negative, the game Shuts Down
8- If Replay Positive, the game Starts at 1-
'''
import random
import string
#from IPython.display import clear_output
def playtictactoe():
    """
    The RUN function of this program. Deploys the board,
    receives the players input, and makes the necessary calls.
    """
    print("\n~~~ Welcome to Tic Tac Toe! ~~~\n")
    gameison = False
    firstplayer = choose_first()
    p1mrk, p2mrk = player_input(firstplayer)
    nextplayer = firstplayer
    board = [' ']*10
    display_board(board)
    gameboard = board
    gameison = True
    marker = ''
    while gameison:
        if nextplayer == 'Player1':
            marker = p1mrk
            player1pos = player_choice(gameboard, nextplayer)
            place_marker(gameboard, marker, player1pos)
            display_board(gameboard)
            if win_check(gameboard, marker):
                print(f'\n~~~ {nextplayer} WON THE GAME! ~~~\n')
                replay()
            if full_board_check(gameboard):
                print('\n~~~ DRAW ~~~\n!')
                replay()
            else:
                nextplayer = 'Player2'
        elif nextplayer == 'Player2':
            marker = p2mrk
            player2pos = player_choice(gameboard, nextplayer)
            place_marker(gameboard, marker, player2pos)
            display_board(gameboard)
            if win_check(gameboard, marker):
                print(f'\n~~~ {nextplayer} WON THE GAME! ~~~\n')
                replay()
            if full_board_check(gameboard):
                print('\n~~~ DRAW ~~~\n')
                replay()
            else:
                nextplayer = 'Player1'
        else:
            break
def choose_first():
    """
    Function that randomly returns who goes first (Player1 or Player2).
    """
    if random.randint(1, 2) == 1:
        print('Choosing random Player to start...')
        print('\n >> Player1 goes first! << \n')
        first_player = 'Player1'
    else:
        print('Choosing random Player to start...')
        print('\n >> Player2 goes first! << \n')
        first_player = 'Player2'
    return first_player
def player_input(player):
    """
    Function that asks the first Player to choose a marker 'X' or 'O' and returns it.
    """
    markerchoice = ''
    while markerchoice.lower() != 'x' and markerchoice.lower() != 'o':
        markerchoice = input(f'{player} wants X or O? ')
        firstplayermarker = markerchoice.upper()
        if player == 'Player1':
            p1marker = firstplayermarker
            if p1marker == 'X':
                p2marker = 'O'
            else:
                p2marker = 'X'
        elif player == 'Player2':
            p2marker = firstplayermarker
            if p2marker == 'X':
                p1marker = 'O'
            else:
                p1marker = 'X'
    return(p1marker, p2marker)
def display_board(board):
    """
    Function that resets the view (adds 100 blank lines) and
    displays the board with the Players markers.
    """
    #from IPython.display import clear_output
    #clear_output()
    print('\n' * 100)
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('---------')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('---------')
    print(board[1]+' | '+board[2]+' | '+board[3])
def player_choice(board, player):
    """
    Function that asks the Player for the position of his/hers next move,
    checks if it is allowed and returns the position.
    """
    position = 0
    digitset = set(string.digits)
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not is_space_free(board, position):
        position = (input(f'{player} choose your next position: (1-9) '))
        if position in digitset:        # to catch int casting on letters and symbols
            position = int(position)
        else:
            print('Invalid char! Choose 1-9!')
    return position
def is_space_free(board, position):
    """
    Function that checks if a space is free on the board.
    """
    return not(board[position] == 'X' or board[position] == 'O')
def place_marker(board, marker, position):
    """
    Function that places a marker in a given on the board.
    """
    board[position] = marker
def win_check(board, marker):
    """
    Function that checks if a Player has won.
    """
    return ((board[7] == marker and board[8] == marker and board[9] == marker) or
            (board[4] == marker and board[5] == marker and board[6] == marker) or
            (board[1] == marker and board[2] == marker and board[3] == marker) or
            (board[7] == marker and board[4] == marker and board[1] == marker) or
            (board[8] == marker and board[5] == marker and board[2] == marker) or
            (board[9] == marker and board[6] == marker and board[3] == marker) or
            (board[7] == marker and board[5] == marker and board[3] == marker) or
            (board[9] == marker and board[5] == marker and board[1] == marker))
def full_board_check(board):
    """
    Function that checks if a draw has happened.
    """
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True
def replay():
    """
    Function that asks the Players if they want to play again, and shuts down otherwise.
    """
    replayornot = ''
    while replayornot != 'y' or replayornot != 'n':
        replayornot = input('Do you want to play again? (y/n): ')
        if replayornot == 'y':
            playtictactoe()
            break
        elif replayornot == 'n':
            print('Shutting down...')
            exit()
            break

if __name__ == "__main__":
    playtictactoe()
