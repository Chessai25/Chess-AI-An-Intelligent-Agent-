import random

# Chess symbols (same as in the HTML)
PIECES = {
    'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚', 'p': '♟',
    'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙'
}

# Initial board setup
initial_board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

class ChessGame:
    def __init__(self):
        self.board = [row[:] for row in initial_board]
        self.current_player = 'white'
        self.selected_square = None
        self.valid_moves = []
        self.game_over = False
        self.status = "White's turn"
    
    def print_board(self):
        for row in self.board:
            print(' '.join([PIECES.get(piece, ' ') for piece in row]))
    
    def is_valid_move(self, from_row, from_col, to_row, to_col):
        # Check if the move is valid (similar to the logic in the JavaScript)
        piece = self.board[from_row][from_col]
        if piece == ' ':
            return False
        
        # Handle capturing logic and basic piece movements here, similar to JS code.
        # Simplified version, not checking for check or checkmate.

        return True

    def make_move(self, from_row, from_col, to_row, to_col):
        piece = self.board[from_row][from_col]
        self.board[to_row][to_col] = piece
        self.board[from_row][from_col] = ' '
        # Switch player
        self.current_player = 'black' if self.current_player == 'white' else 'white'
        self.status = f"{self.current_player.capitalize()}'s turn"
    
    def ai_move(self):
        # Simple AI: Random valid move for black
        valid_moves = []
        for from_row in range(8):
            for from_col in range(8):
                piece = self.board[from_row][from_col]
                if piece != ' ' and piece.islower():  # Black pieces
                    for to_row in range(8):
                        for to_col in range(8):
                            if self.is_valid_move(from_row, from_col, to_row, to_col):
                                valid_moves.append((from_row, from_col, to_row, to_col))
        
        if valid_moves:
            move = random.choice(valid_moves)
            self.make_move(*move)

    def handle_move(self, move):
        if self.game_over:
            return
        
        # Parse move in algebraic notation (e.g., 'e2e4')
        if len(move) < 4:
            print("Invalid move format (e.g. e2e4)")
            return
        
        start_col, start_row = ord(move[0]) - ord('a'), 8 - int(move[1])
        end_col, end_row = ord(move[2]) - ord('a'), 8 - int(move[3])
        
        if not (0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8):
            print("Invalid coordinates.")
            return

        # Validate and make the move
        if self.is_valid_move(start_row, start_col, end_row, end_col):
            self.make_move(start_row, start_col, end_row, end_col)
            self.print_board()
            
            # AI move after human move
            if not self.game_over and self.current_player == 'black':
                self.ai_move()
                self.print_board()
        else:
            print("Invalid move!")

# Initialize the game
game = ChessGame()

# Main game loop
while not game.game_over:
    game.print_board()
    print(game.status)
    move = input("Enter move (e.g. e2e4): ").strip().lower()
    game.handle_move(move)
