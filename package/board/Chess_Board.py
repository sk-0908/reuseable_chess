from ..pieces.Piece import Piece
from ..pieces.pieces_of_chess.Pawn import Pawn
from ..pieces.pieces_of_chess.Knight import Knight
from ..pieces.pieces_of_chess.Bishop import Bishop
from ..pieces.pieces_of_chess.Rook import Rook
from ..pieces.pieces_of_chess.Queen import Queen
from ..pieces.pieces_of_chess.King import King

class ChessBoard:
    def __init__(self):
        # チェスボードの初期化
        self.board = [[' ' for _ in range(8)] for _ in range(8)]

        # 駒の配置
        self.initialize_pieces()

    def initialize_pieces(self):
        for i in range(8):
            self.board[1][i] = Pawn('white')
            self.board[6][i] = Pawn('black')

        # 他の駒の初期配置
        self.board[0][0] = Rook('white')
        self.board[0][1] = Knight('white')
        self.board[0][2] = Bishop('white')
        self.board[0][3] = Queen('white')
        self.board[0][4] = King('white')
        self.board[0][5] = Bishop('white')
        self.board[0][6] = Knight('white')
        self.board[0][7] = Rook('white')

        self.board[7][0] = Rook('black')
        self.board[7][1] = Knight('black')
        self.board[7][2] = Bishop('black')
        self.board[7][3] = Queen('black')
        self.board[7][4] = King('black')
        self.board[7][5] = Bishop('black')
        self.board[7][6] = Knight('black')
        self.board[7][7] = Rook('black')


    def display_board(self):
    # 列のアルファベットを表示
        print("  A B C D E F G H")

        for i, row in enumerate(self.board):
            # 行の数字を表示
            print(f"{8-i} ", end="")
            
            for piece in row:
                print(f"{piece} ", end="")
            
            print()  # 改行
    
    def capture_piece(self, square):
        row, col = square
        captured_piece = self.board[row][col]
        self.board[row][col] = ' '  # 相手の駒を取るので空にする
        return captured_piece

    def use_captured_piece(self, square, new_piece):
        row, col = square
        self.board[row][col] = new_piece

    def remove_piece(self, square):
        row, col = square
        self.board[row][col] = ' '

    def get_piece_at_coordinates(self, coordinates):
        """
        指定された座標にある駒を取得します。
        :param coordinates: 座標（例: "a3"）
        :return: 駒のインスタンスまたは None
        """
        col = ord(coordinates[0]) - ord('a')
        row = int(coordinates[1]) - 1

        if 0 <= row < 8 and 0 <= col < 8:
            return self.board[row][col]
        else:
            return None
