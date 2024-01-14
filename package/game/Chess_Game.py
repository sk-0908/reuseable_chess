from ..pieces.Piece import Piece
from ..board.Chess_Board import ChessBoard
from ..pieces.pieces_of_chess import Pawn , Knight , Bishop , Rook , Queen , King

class ChessGame:
    def __init__(self):
        # ChessBoardオブジェクトを作成
        self.chess_board = ChessBoard()
        # ターンを管理する変数
        self.current_turn = 'white'
        # 手の履歴を保存するためのリスト
        self.moves_history = []  

    def is_game_over(self):
        white_king_found = False
        black_king_found = False

        for row in range(len(self.chess_board.board)):
            for col in range(len(self.chess_board.board[row])):
                piece = self.chess_board.board[row][col]

                if isinstance(piece, Piece):
                    if piece.is_king() and piece.color == 'white':
                        white_king_found = True
                    elif piece.is_king() and piece.color == 'black':
                        black_king_found = True

        # どちらかのキングが見つからない場合はゲーム終了（取られた側の負け）
        return not white_king_found or not black_king_found

    def is_valid_move(self, start_row, start_col, end_row, end_col):
        # 駒の動きが妥当かどうかの検証ロジックを追加
        piece_at_start = self.chess_board.board[start_row][start_col]
        if piece_at_start is not None:
            return piece_at_start.valid_moves((start_row, start_col), (end_row, end_col), self.chess_board.board)
        else:
            return False

    def play(self):
        while not self.is_game_over():
            def invalid_input():
                print("This is invalid input")

            def is_valid_input(user_input):
                if self.chess_board.get_piece_at_coordinates(user_input):
                    if len(user_input) == 2:
                        # 文字が'A'から'H'の範囲内かどうかを確認
                        if user_input[0].upper() in 'ABCDEFGH':
                            # 数字が1から8の範囲内かどうかを確認
                            if user_input[1].isdigit() and 1 <= int(user_input[1]) <= 8:
                                return True

                return False
            while True:
                # ボードの表示
                print("\nCurrent Board:")
                self.chess_board.display_board()

                # ターンの表示
                print(f"\n{self.current_turn}'s turn.")

                # ユーザーに駒の座標と動かす場所の座標を入力させる
                #入力が不正でないか
                while True:
                    start_square = input("Enter the coordinates of the piece you want to move (e.g., 'A2')")
                    if is_valid_input(start_square):
                        break
                    else:
                        invalid_input()
                while True:
                    end_square = input("Enter the coordinates where you want to move the piece (e.g., 'B4'):")
                    if is_valid_input(end_square) and start_square != end_square:
                        break
                    else:
                        invalid_input()

                # 入力された座標に基づいて駒を動かす
                self.move_piece(start_square, end_square)

                # ターンを切り替える
                self.switch_turn()


    def move_piece(self, start_square, end_square):
        # 入力された座標を変換して、駒を動かす
        start_row, start_col = self.convert_coordinates(start_square)
        end_row, end_col = self.convert_coordinates(end_square)

        # 駒の動きを検証し、移動が可能であれば駒を動かす
        if not self.is_valid_move(start_row, start_col, end_row, end_col):
            moving_piece = self.chess_board.board[start_row][start_col]
            self.chess_board.board[start_row][start_col] = ' '
            self.chess_board.board[end_row][end_col] = moving_piece
        else:
            print("Invalid move. Try again.")

        # 新しい手を手の履歴に追加
        self.moves_history.append((start_square, end_square))

    def convert_coordinates(self, square):
        # ユーザーが入力した座標（例: 'A2'）を内部の座標に変換するロジックを追加
        return 8 - int(square[1]), ord(square[0].upper()) - ord('A')

    def switch_turn(self):
        # ターンを切り替えるロジックを追加
        self.current_turn = 'black' if self.current_turn == 'white' else 'white'