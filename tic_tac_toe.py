# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 14:06:09 2020

@author: rafaw
"""
#
import os


row_specifiers = ['X', 'Y', 'Z']
#correlating first coord [X, Y, Z] with numbers respectively[1, 2, 3]
cord_dict = {'X': 0, 'Y': 1, 'Z': 2}
current_user = 'user1'
user_names = {'user1': 'User 1', 'user2': 'User 2'}

def display_board():
    i=0
    print('      1 2 3\n')
    for row in board:
        print(f'{row_specifiers[i]}    |', end='')
        for column in board[i][:]:
            print(column, end='|')  
        i += 1
        print('\n')

def clear():
    #print('\n'*100)
    print('\n'*100)
    
def user_input():
    choice = 'wrong'
    i = 0
    while choice not in ['X', 'O', 'x', 'o']:
        clear()
        if i > 0:
            print('You entered wrong input')
        if choice.isdigit():
            print('Why would you try to enter a number?')
        choice = input('User 1: Do you want to be X or O? Type X or O\n')
        i += 1
    
    #assign users' markers
    choice = choice.upper()
    if choice == 'X':
        marker_user2 = 'O'
    else:
        marker_user2 = 'X'
    
    #make a dictionary of markers
    d = {'user1': choice, 'user2': marker_user2}
    return d

def input_coordinates(board):
    first_coord = 'wrong'
    second_coord = 'wrong'
    i = 0
    clear()
    display_board()
    
    while True: 
        choice = input(f'{user_names[current_user]}: Enter coordinates, e. g. X2\n')
        
        #wrong input handling
        #print warning when input error
        if i>0: 
            print('You entered wrong input!')
        #check if input is in correct format
        if len(choice) == 2:
            if choice[0].isalpha():
                first_coord = choice[0].upper()
            if choice[1].isdigit():
                second_coord = int(choice[1])
            if first_coord not in row_specifiers or not choice[0].isalpha():
                print('First coordinate is wrong. The first character must be X, Y or Z')
            if second_coord not in range(1,4) or not choice[1].isdigit():
                print('Second coordinate is wrong. The second character must be an integer in range [1,3]')
        else:
            print('Wrong length of input: input must consist of 2 characters')
            
        #checking if spot is empty
        if (first_coord in row_specifiers and second_coord in [1,2,3]):
            if board[cord_dict[first_coord]][second_coord-1] == '-':
                break
            else:
                print('This place is already occupied')
                first_coord = 'wrong'
                second_coord = 'wrong'
           
        i += 1
    
    return (first_coord, second_coord)
        
def place_marker(board, marker, coordinates):
    
    #changing board    
    board[cord_dict[coordinates[0]]][coordinates[1]-1] = marker
    
        
def win_check(board, mark):
    list_of_win_marks = [mark, mark, mark]
    
    #checking rows
    if list_of_win_marks in board: 
        return True
    
    #checking collumns    
    for i in range(0, len(board[0][:])):
        column = [board[0][i], board[1][i], board[2][i]]
        if column == list_of_win_marks:
            return True
    
    #checking diagonals
    diagonal1 = [board[0][0], board[1][1], board[2][2]]
    diagonal2 = [board[2][0], board[1][1], board[0][2]]
    if diagonal1 == list_of_win_marks or diagonal2 == list_of_win_marks:
        return True
    
    return False
    
def full_board_check():
    i=0
    for row in board:
        #searching every spot in a row
        for spot in board[i][:]:
            #return true if there is a spot left
            if spot == '-':
                return True
        i += 1
    
    return False

def replay():
    i = 0
    while True:
        if i>0:
            print('Wrong input!')
        choice = input('Do you want to play again? [Y/N]')
        if choice.isalpha():
            choice = choice.upper()
        if choice == 'Y':
            return True
        elif choice == 'N':
            return False
        i += 1
        
    



while True:
    i = 0
    clear()
    board = [['-','-','-'],\
             ['-','-','-'],\
             ['-','-','-']]
    current_user = 'user1'
    marker_dict = user_input()
    play = True
    
    while play:
        display_board()
        coordinates = input_coordinates(board)
        place_marker(board, marker_dict[current_user], coordinates)
        
        #stop if someone won
        if win_check(board, marker_dict[current_user]):
            clear()
            display_board()
            print(f"{user_names[current_user]} with marker '{marker_dict[current_user]}' won!")
            play = False
            
        #stop if there's no room on board
        if not full_board_check():
            clear()
            display_board()
            print("It's a tie!")
            play = False
            
        #switching the user
        if current_user == 'user1':
            current_user = 'user2'
        else:
            current_user = 'user1'
        
        if play:
            clear()
            
        i += 1
    if not replay():
        break

        
    


