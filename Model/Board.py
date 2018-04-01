import random


def clear_output():
    print('\n' * 100)


class Board:
    board = ["-" for i in range(9)]
    markers = {}
    firstPlayer = 0

    def game_launch(self):
        self.game_start()
        choose_first()
        self.display_board()
        player_input(self.firstPlayer)
        self.display_board()

    '''
    NOTE: add clear output functionality later
    
    sets up the game board and takes in a list and places it at indexed locations
    index of game board follows numpad alignment:
    7|8|9
    4|5|6
    1|2|3
    '''

    def display_board(self):
        print(' ' + ' ' + '|' + ' ' + ' ' + ' ' + '|' + ' ' + ' ')
        print(Board.board[7] + ' ' + '|' + ' ' + Board.board[8] + ' ' + '|' + ' ' + Board.board[9])
        print(' ' + ' ' + '|' + ' ' + ' ' + ' ' + '|' + ' ' + ' ')
        print('-' * 9)
        print(' ' + ' ' + '|' + ' ' + ' ' + ' ' + '|' + ' ' + ' ')
        print(Board.board[4] + ' ' + '|' + ' ' + Board.board[5] + ' ' + '|' + ' ' + Board.board[6])
        print(' ' + ' ' + '|' + ' ' + ' ' + ' ' + '|' + ' ' + ' ')
        print('-' * 9)
        print(' ' + ' ' + '|' + ' ' + ' ' + ' ' + '|' + ' ' + ' ')
        print(Board.board[1] + ' ' + '|' + ' ' + Board.board[2] + ' ' + '|' + ' ' + Board.board[3])
        print(' ' + ' ' + '|' + ' ' + ' ' + ' ' + '|' + ' ' + ' ')

    def game_start(self):
        print('Welcome to Tic Tac Toe!')
        print('\n')
        while True:
            player1 = input('Player 1: Choose your marker (X or O)')
            if player1 != 'X' or 'O':
                print('Please choose valid marker')
                continue
            else:
                print("Player 1's marker is: " + player1)
                break
        if player1 is 'X':
            player2 = 'O'
        else:
            player2 = 'X'
        Board.markers = {1: player1, 2: player2}

def choose_first():
    x = random.randint(0, 20)
    if x % 2 == 0:
        print("Player 1 goes first!")
        firstPlayer = 1
    else:
        print("Player 2 goes first!")
        firstPlayer = 2


def player_input(player):
    marker = Board.markers.get(player)
    while True:
        position = int(input("Select position (1 to 9"))
        if position != 0 <= position <= 9:
            print("Please select valid position")
            continue
    else:
        break
    place_marker(marker, position)


def place_marker(marker, position):
    Board.board[position] = marker


def win_check(board,marker):
    pass
