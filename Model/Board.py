def clear_output():
    print('\n' * 100)


'''
NOTE: add clear output functionality later

sets up the game board and takes in a list and places it at indexed locations
index of game board follows numpad alignment:
7|8|9
4|5|6
1|2|3
'''
def display_board(board):
    print(' ' + ' ' + '|' + ' ' + ' ' + ' ' + '|' + ' ' + ' ')
    print(board[7] + ' ' + '|' + ' ' + board[8] + ' ' + '|' + ' ' + board[9])
    print(' ' + ' ' + '|' + ' ' + ' ' + ' ' + '|' + ' ' + ' ')
    print('-' * 9)
    print(' ' + ' ' + '|' + ' ' + ' ' + ' ' + '|' + ' ' + ' ')
    print(board[7] + ' ' + '|' + ' ' + board[8] + ' ' + '|' + ' ' + board[9])
    print(' ' + ' ' + '|' + ' ' + ' ' + ' ' + '|' + ' ' + ' ')
    print('-' * 9)
    print(' ' + ' ' + '|' + ' ' + ' ' + ' ' + '|' + ' ' + ' ')
    print(board[7] + ' ' + '|' + ' ' + board[8] + ' ' + '|' + ' ' + board[9])
    print(' ' + ' ' + '|' + ' ' + ' ' + ' ' + '|' + ' ' + ' ')
