from src.settings import *

class Game:
    def __init__(self) -> None:
        self.board = create_board()
        self.gameover = False
        self.turn = 0
    
    def run(self):
        while not self.gameover:
            if self.turn == 0:
                col = int(input("[?] Player 1 make your Selection (0-6): "))
                print("[!] Player 1 select: ", col)

                if col > 6:
                    print("[x] Error your number is to high!")
                elif col < 0:
                    print("[x] Error your number is to low!")

                if self.is_valid_location(self.board, col):
                    row = self.get_next_open_row(self.board, col)
                    self.drop_piece(self.board, row, col, 1)
                    if self.winning_move(self.board, 1):
                        print("[!] Player 1 Wins!")
                        time.sleep(2)
                        self.gameover = True
                        return
                        
            else:
                col = int(input("[?] Player 2 make your Selection (0-6): "))
                print("[!] Player 2 select: ", col)

                if col > 6:
                    print("[x] Error your number is to high!")
                elif col < 0:
                    print("[x] Error your number is to low!")

                if self.is_valid_location(self.board, col):
                    row = self.get_next_open_row(self.board, col)
                    self.drop_piece(self.board, row, col, 2)
                    if self.winning_move(self.board, 2):
                        print("[!] Player 2 Wins!")
                        time.sleep(2)
                        self.gameover = True
                        return
                
            self.turn += 1
            self.turn = self.turn % 2
            self.print_board(self.board)
        os.system("cls")
        option = input("[?] Wanna restart (Y/N): ")
        if option == "":
            return
        elif option.upper() == 'Y':
            self.reset_game()
        else:
            return
            
    
    def print_board(self, board):
        print(np.flip(board, 0))

    def is_valid_location(self, board, col):
        return board[ROW_COUNT - 1][col] == 0

    def drop_piece(self, board, row, col, piece):
        board[row][col] = piece
    
    def get_next_open_row(self, board, col):
        for r in range(ROW_COUNT):
            if board[r][col] == 0:
                return r

    def winning_move(self, board, piece) -> bool:
        # Check horizontal locations
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT):
                if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                    return True

        # Check Vertical locations
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 3):
                if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                    return True

        # Check diagonals right
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                    return True
        
        # Check diagonals left
        for c in range(COLUMN_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                    return True
        return False

    def reset_game(self):
        print("[!] Reset Game!")
        self.turn = 0
        self.gameover = False
        self.board = create_board()
        # self.run()


