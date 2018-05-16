def playtictactoe():
    
    gameison = False
    firstplayer = choose_first()
    p1mrk, p2mrk = player_input(firstplayer)
    
    nextplayer = firstplayer
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    display_board(board)
    gameboard = board
    gameison = True
    marker = ''
    
    while gameison == True:
        
        
        if win_check(gameboard) == True:
            print(f'{marker} WON THE GAME')
            replay()
        
        #if full_board_check(gameboard) == True:
            #replay()
        
        if nextplayer == 'Player1':
            marker = p1mrk
            player1pos = player_choice(gameboard, nextplayer)
            place_marker(gameboard, marker, player1pos)
            display_board(gameboard)
            nextplayer = 'Player2'
            win_check(gameboard)
            #full_board_check(gameboard)
            pass
        elif nextplayer == 'Player2':
            marker = p2mrk
            player2pos = player_choice(gameboard, nextplayer)
            place_marker(gameboard, marker, player2pos)
            display_board(gameboard)
            nextplayer = 'Player1'
            win_check(gameboard)
            #full_board_check(gameboard)
            pass
        
       
        else:
            break
            
import random

def choose_first():
    if random.randint(1,2) == 1:
        return 'Player1'
    else:
        return 'Player2'
    
def player_input(player):
    
    markerchoice = '' 
    while markerchoice != 'X' and markerchoice != 'O':
        markerchoice = input(f'{player} wants X or O? ')
        p1marker = markerchoice
        if p1marker == 'X':
            p2marker = 'O'
        else:
            p2marker = 'X'
    
    return(p1marker,p2marker)


from IPython.display import clear_output

def display_board(board):
    #from IPython.display import clear_output
    #clear_output()
    print('\n' * 100) # <== for IDEs
    
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('---------')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('---------')
    print(board[1]+' | '+board[2]+' | '+board[3])
    
    


def place_marker(board, marker, position):
    
    board[position] = marker
    
    
def win_check(board):    
    if board[1] == 'X' and board[2]== 'X' and board[3] == 'X':
        return True
    if board[4] == 'X' and board[5]== 'X' and board[6] == 'X':
        return True
    if board[7] == 'X' and board[8]== 'X' and board[9] == 'X':
        return True
    if board[1] == 'X' and board[4]== 'X' and board[7] == 'X':
        return True
    if board[2] == 'X' and board[5]== 'X' and board[8] == 'X':
        return True
    if board[3] == 'X' and board[6]== 'X' and board[9] == 'X':
        return True
    if board[1] == 'X' and board[5]== 'X' and board[9] == 'X':
        return True
    if board[3] == 'X' and board[5]== 'X' and board[7] == 'X':
        return True
    
    if board[1] == 'O' and board[2]== 'O' and board[3] == 'O':
        return True
    if board[4] == 'O' and board[5]== 'O' and board[6] == 'O':
        return True
    if board[7] == 'O' and board[8]== 'O' and board[9] == 'O':
        return True
    if board[1] == 'O' and board[4]== 'O' and board[7] == 'O':
        return True
    if board[2] == 'O' and board[5]== 'O' and board[8] == 'O':
        return True
    if board[3] == 'O' and board[6]== 'O' and board[9] == 'O':
        return True
    if board[1] == 'O' and board[5]== 'O' and board[9] == 'O':
        return True
    if board[3] == 'O' and board[5]== 'O' and board[7] == 'O':
        return True
    
    else:
        return False
        

    
def is_space_free(board, position):
    if board[position] == 'X' or board[position] == 'O':
        return False
    else:
        return True
    
    
def full_board_check(board):
    i=0
    counter=0
    while i > len(board):
        isthisfree = is_space_free(board,i)
        if isthisfree == False:
            counter+=1
            i+=1
        else:
            i+=1
    if counter == 9:
        return True
    else:
        return False
            
def player_choice(board, player):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not is_space_free(board, position):
        position = int(input(f'{player} choose your next position: (1-9) '))
        
    return position
        
        
def replay():
    replayornot = ''
    while replayornot != 'y' or replayornot != 'n':
        replayornot = input('Do you want to play again? (y/n): ')
        if replayornot == 'y':
            playtictactoe()
            break
        elif replayornot == 'n':
            print('Shutting down...')
            break

playtictactoe()