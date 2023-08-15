import random

class TicTacToe:
    def __init__(self):
        self.board = [[' '] * 3 for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print(' | '.join(row))
            print('-' * 9)

    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False

    def check_winner(self):
        symbol = self.current_player
        for i in range(3):
            if all(self.board[i][j] == symbol for j in range(3)) or \
                    all(self.board[j][i] == symbol for j in range(3)):
                return True
        return all(self.board[i][i] == symbol for i in range(3)) or \
               all(self.board[i][2 - i] == symbol for i in range(3))

    def check_draw(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def validate_input(self, row, col):
        return 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' '

    def player_turn(self):
        while True:
            self.print_board()
            try:
                row, col = map(int, input(f"Player {self.current_player}, enter row and column (0-2): ").split())
                if self.validate_input(row, col):
                    if self.make_move(row, col):
                        if self.check_winner():
                            self.print_board()
                            print(f"Player {self.current_player} wins!")
                            return 'win'
                        elif self.check_draw():
                            self.print_board()
                            print("It's a draw!")
                            return 'draw'
                        self.switch_player()
                        return 'continue'
                    else:
                        print("Cell already occupied. Try again.")
                else:
                    print("Invalid input. Row and column must be 0, 1, or 2.")
            except ValueError:
                print("Invalid input. Enter integers for row and column.")

    def computer_turn(self):
        # Try to win
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'O'  # Simulate computer's move
                    if self.check_winner():
                        self.switch_player()  # Switch back to player before returning
                        return 'win'
                    self.board[i][j] = ' '  # Undo the simulated move

        # Block player's winning move
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'X'  # Simulate player's move
                    self.switch_player()
                    if self.check_winner():
                        self.board[i][j] = 'O'  # Block the winning move
                        return 'continue'
                    self.switch_player()
                    self.board[i][j] = ' '  # Undo the simulated move

        # Make a rational move
        for i in [1, 0, 2]:  # Rational row order
            for j in [1, 0, 2]:  # Rational column order
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'O'
                    if self.check_winner():
                        self.board[i][j] = ' '  # Undo move if it causes a win
                        continue
                    self.switch_player()  # Switch back to player before returning
                    return 'continue'

        self.switch_player()  # If no move is made, still switch back to player
        return 'continue'

    def play(self):
        while True:
            if self.current_player == 'X':
                status = self.player_turn()
            else:
                status = self.computer_turn()

            if status == 'win':
                self.print_board()
                if self.current_player == 'X':
                    print("Player wins!")
                else:
                    print("Computer wins!")
                break
            elif status == 'draw':
                self.print_board()
                print("It's a draw!")
                break


if __name__ == "__main__":
    game = TicTacToe()
    game.play()
