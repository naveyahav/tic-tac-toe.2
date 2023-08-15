class TicTacToe:
    def __init__(self):
        # Initialize the game board and current player
        self.board = [[' '] * 3 for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        # Display the game board
        for row in self.board:
            print(' | '.join(row))
            print('-' * 9)

    def switch_player(self):
        # Switch the current player's turn
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def make_move(self, row, col):
        # Make a move on the board if the cell is empty
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True  # Move was successful
        return False  # Cell was already occupied

    def check_winner(self):
        # Check if the current player has won
        symbol = self.current_player
        for i in range(3):
            if all(self.board[i][j] == symbol for j in range(3)) or \
                    all(self.board[j][i] == symbol for j in range(3)):
                return True  # Win by row or column
        return all(self.board[i][i] == symbol for i in range(3)) or \
               all(self.board[i][2 - i] == symbol for i in range(3))  # Win by diagonal

    def check_draw(self):
        # Check if the game is a draw (all cells filled)
        return all(cell != ' ' for row in self.board for cell in row)

    def validate_input(self, row, col):
        # Validate that the input is within the board and the cell is empty
        return 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' '

    def play(self):
        while True:
            self.print_board()
            try:
                row, col = map(int, input(f"Player {self.current_player}, enter row and column (0-2): ").split())
                if self.validate_input(row, col):
                    if self.make_move(row, col):
                        if self.check_winner():
                            self.print_board()
                            print(f"Player {self.current_player} wins!")
                            break
                        elif self.check_draw():
                            self.print_board()
                            print("It's a draw!")
                            break
                        self.switch_player()
                    else:
                        print("Cell already occupied. Try again.")
                else:
                    print("Invalid input. Row and column must be 0, 1, or 2.")
            except ValueError:
                print("Invalid input. Enter integers for row and column.")


if __name__ == "__main__":
    game = TicTacToe()
    game.play()

