import random


def clear_output():
    print('\n' * 100)





class Board:
    board = ["-" for i in range(9)]
    markers = {}
    players = [0, 0]
    hasWon = False
    fullBoard = False
    winner = 0

    def game_launch(self):
        self.game_start()
        self.choose_first()
        self.display_board()

        while not (self.fullBoard or self.hasWon):
            for i in self.players:
                self.full_board_check()
                self.win_check()
                self.player_input(i)
                self.display_board()

        if self.hasWon:
            print("Player " + str(self.winner) + " has won!!")
            print("Congratulations!")

        elif self.fullBoard:
            print("Full board, it's a tie!")

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
        print(self.board[6] + ' ' + '|' + ' ' + self.board[7] + ' ' + '|' + ' ' + self.board[8])
        print(' ' + ' ' + '|' + ' ' + ' ' + ' ' + '|' + ' ' + ' ')
        print('-' * 9)
        print(' ' + ' ' + '|' + ' ' + ' ' + ' ' + '|' + ' ' + ' ')
        print(self.board[3] + ' ' + '|' + ' ' + self.board[4] + ' ' + '|' + ' ' + self.board[5])
        print(' ' + ' ' + '|' + ' ' + ' ' + ' ' + '|' + ' ' + ' ')
        print('-' * 9)
        print(' ' + ' ' + '|' + ' ' + ' ' + ' ' + '|' + ' ' + ' ')
        print(self.board[0] + ' ' + '|' + ' ' + self.board[1] + ' ' + '|' + ' ' + self.board[2])
        print(' ' + ' ' + '|' + ' ' + ' ' + ' ' + '|' + ' ' + ' ')

    def game_start(self):
        print('Welcome to Tic Tac Toe!')
        print('\n')
        while True:
            player1 = input('Player 1: Choose your marker (X or O)')
            if (player1 != 'X') and (player1 != 'O'):
                print('Please choose valid marker')
                continue
            else:
                break
        if player1 is 'X':
            player2 = 'O'
        else:
            player2 = 'X'
        self.markers = {1: player1, 2: player2}

    def choose_first(self):
        x = random.randint(0, 20)
        if x % 2 == 0:
            print("Player 1 goes first!")
            self.players[0] = 1
            self.players[1] = 2
            # self.firstPlayer = 1
            # self.secondPlayer = 2
            print("Player 1's marker is: " + self.markers.get(1))
        else:
            print("Player 2 goes first!")
            self.players[0] = 2
            self.players[1] = 1
            # self.firstPlayer = 2
            # self.secondPlayer = 1
            print("Player 2's marker is: " + self.markers.get(2))

    def win_check(self):
        if self.board[6] == self.board[7] == self.board[8] in self.markers.values():
            self.hasWon = True
            self.winner = self.get_winner(self.board[6])
        elif self.board[3] == self.board[4] == self.board[5] in self.markers.values():
            self.hasWon = True
            self.winner = self.get_winner(self.board[3])
        elif self.board[0] == self.board[1] == self.board[2] in self.markers.values():
            self.hasWon = True
            self.winner = self.get_winner(self.board[0])

        elif self.board[6] == self.board[4] == self.board[2] in self.markers.values():
            self.hasWon = True
            self.winner = self.get_winner(self.board[6])
        elif self.board[8] == self.board[4] == self.board[0] in self.markers.values():
            self.hasWon = True
            self.winner = self.get_winner(self.board[0])

        elif self.board[6] == self.board[3] == self.board[0] in self.markers.values():
            self.hasWon = True
            self.winner = self.get_winner(self.board[6])
        elif self.board[7] == self.board[4] == self.board[1] in self.markers.values():
            self.hasWon = True
            self.winner = self.get_winner(self.board[4])
        elif self.board[8] == self.board[5] == self.board[2] in self.markers.values():
            self.hasWon = True
            self.winner = self.get_winner(self.board[5])

    def space_check(self, position):
        if (self.board[position] == 'X') or (self.board[position] == 'O'):
            return False
        else:
            return True

    def place_marker(self, marker, position):
        self.board[position] = marker

    def player_input(self, player):
        marker = self.markers.get(player)
        print("Player " + str(player) + "'s turn")
        while True:
            position = int(input("Select position (1 to 9)")) - 1
            if (position not in range(0, 9)) or (not self.space_check(position)):
                print("Please select valid position")
                continue
            else:
                break
        self.place_marker(marker, position)

    def full_board_check(self):
        count = 0
        for x in self.board:
            if x == ('X' or 'O'):
                count += 1

        if count == 9:
            return True

    def get_winner(self, i):
        return list(self.markers.keys())[list(self.markers.values()).index(i)]


def replay():
    while True:
        ans = input("Would you like to start a new game? (y/n)")
        if (ans is not "y") and (ans is not "n"):
            print("Please select valid input")
            continue
        else:
            break

    if ans is "y":
        return True
    else:
        return False


def main():
    while True:
        game = Board()
        game.game_launch()

        if replay():
            clear_output()
            newGame = Board()
            newGame.game_launch()
            pass

        else:
            print("Game Over!")
            print("Goodbye!")
            break


main()
