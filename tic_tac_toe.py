# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 20:36:31 2018

@author: finta
"""

def bord(game):         #this creates a (size x size) board 
    size = len(game)
    game_temp = [[0 for j in range(len(game))] for j in range(len(game))]
    for i in range(len(game)):
        for j in range(len(game)):
            if game[i][j] == 0:
                game_temp[i][j] = ' '
            elif game[i][j] == 1:
                game_temp[i][j] = 'X'
            else:
                game_temp[i][j] = 'O'
    lines = []
    for i in range(len(game)):
        line_temp = '| '
        for j in range(len(game)):
            line_temp = line_temp  + game_temp[i][j] + ' |  '
        lines.append(line_temp) 
    for i in range(0, size):
        print(' --- ' * size)
        print(lines[i])
    print(' --- ' *size)
    #return game
    
def transpose_ttt(matrix):  #this can transpose a square matrix
    result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))]
    return result
    
def check(matrix):      #this checks for a winner
    winner_1 = [1]*len(matrix)
    winner_2 = [2]*len(matrix)
    winner = 0
    
    for i in range(0, len(matrix)):     #first by checking rows
        if matrix[i] == winner_1:
            winner = 1
        elif matrix[i] == winner_2:
            winner = 2
    
    vert = transpose_ttt(matrix)
    
    for i in range(0, len(matrix)):         #then by checking columns
        if vert[i] == winner_1:
            winner = 1
        elif vert[i] == winner_2:
            winner = 2
    
    diag_1 = [matrix[i][i] for i in range(len(matrix))]
    diag_2 = [matrix[i][-(i+1)] for i in range(len(matrix))]
    
    if diag_1 == winner_1 or diag_2 == winner_1:
        winner = 1
    elif diag_1 == winner_2 or diag_2 == winner_2:
        winner = 2
    
    
    return winner


def move(game, player):
    while True:
        inp = input('Player ' + str(player+1) + ' please input the coordinates of your next move, seperated by a comma: ')
        if inp == 'quit':
            game = 'quit'
            return game
        else:
            coord = [int(inp[0]), int(inp[len(inp)-1])]
            try:
                if game[coord[0]-1][coord[1]-1] == 0:
                    game[coord[0]-1][coord[1]-1]= player+1
                    break
                else:
                    print('Sorry that square is alrady taken! Try again.')
            except IndexError:
                print('Out of range! Try again.')
    return game

if __name__ == '__main__':
    
    #Q = False
    print('Type \'quit\' at any point to quit.')
    while True:   
        size = input('Please enter the size of your tic-tac-toe game: ')
        if size == 'quit':
            break
        else:
            size = int(size)
            winner = 0
            counter = 1
            player = 1
            game = [[0 for j in range(size)] for j in range(size)]
     
        while winner == 0 and counter <= size*size:
            player +=1
            game = move(game, player%2)
            if game == 'quit':
                break
            bord(game)
            winner = check(game)
            counter += 1
        if game == 'quit':
            break
        elif winner == 0:
            print('Draw!')
            break
        else:
            player = player%2+1
            print('Congradulations player', player, 'you win!')
            break
    
        
    

