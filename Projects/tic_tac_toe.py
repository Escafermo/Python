import random
import string
from IPython.display import clear_output

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

def playtictactoe():
    
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
    
    while gameison == True:
        
        if nextplayer == 'Player1':
            marker = p1mrk
            player1pos = player_choice(gameboard, nextplayer)
            place_marker(gameboard, marker, player1pos)
            display_board(gameboard)
            if win_check(gameboard,marker):
                print(f'\n~~~ {nextplayer} WON THE GAME! ~~~\n')
                replay()
            if full_board_check(gameboard):
                print('\n~~~ DRAW ~~~\n!')
                replay()
            else:
                nextplayer = 'Player2'
                pass
        elif nextplayer == 'Player2':
            marker = p2mrk
            player2pos = player_choice(gameboard, nextplayer)
            place_marker(gameboard, marker, player2pos)
            display_board(gameboard)
            if win_check(gameboard,marker):
                print(f'\n~~~ {nextplayer} WON THE GAME! ~~~\n')
                replay()
            if full_board_check(gameboard):
                print('\n~~~ DRAW ~~~\n')
                replay()
            else:
                nextplayer = 'Player1'
                pass
        else:
            break

def choose_first():
    if random.randint(1,2) == 1:
        print('Choosing random Player to start...')
        print('\n >> Player1 goes first! << \n')
        return 'Player1'
    else:
        print('Choosing random Player to start...')
        print('\n >> Player2 goes first! << \n')
        return 'Player2'
    
def player_input(player):
    
    markerchoice = '' 
    while markerchoice.lower() != 'x' and markerchoice.lower() != 'o':
        markerchoice = input(f'{player} wants X or O? ')
        p1marker = markerchoice.upper()
        if p1marker == 'X':
            p2marker = 'O'
        else:
            p2marker = 'X'
    
    return(p1marker,p2marker)

def display_board(board):
    #from IPython.display import clear_output
    #clear_output()
    print('\n' * 100) # <== for IDEs
    
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('---------')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('---------')
    print(board[1]+' | '+board[2]+' | '+board[3])


def player_choice(board, player):
    position = 0
    digitset=set(string.digits)
    while position not in [1,2,3,4,5,6,7,8,9] or not is_space_free(board, position):
        position = (input(f'{player} choose your next position: (1-9) '))
        if position in digitset:        # to catch int casting on letters and symbols
            position = int(position)
        else:
            print('Invalid char! Choose 1-9!')
    return position
    
def is_space_free(board, position):
    return not(board[position] == 'X' or board[position] == 'O')


def place_marker(board, marker, position):
    board[position] = marker
    
def win_check(board,marker):    
    return ((board[7] == marker and board[8] == marker and board[9] == marker) or 
    (board[4] == marker and board[5] == marker and board[6] == marker) or 
    (board[1] == marker and board[2] == marker and board[3] == marker) or 
    (board[7] == marker and board[4] == marker and board[1] == marker) or 
    (board[8] == marker and board[5] == marker and board[2] == marker) or 
    (board[9] == marker and board[6] == marker and board[3] == marker) or 
    (board[7] == marker and board[5] == marker and board[3] == marker) or 
    (board[9] == marker and board[5] == marker and board[1] == marker)) 
    
def full_board_check(board):
    for i in range(1,10):
        if is_space_free(board,i):
            return False
    return True
        
def replay():
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
