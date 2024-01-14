from ..Piece import Piece

class Pawn(Piece):
    def __str__(self):
        return 'p' if self.color == 'black' else 'P'
    
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end

        # ポーンの動きの制約を追加
        if self.color == 'white':
            # 白のポーンは前方に1マス進むか、初期位置の場合は2マス進むことができる
            if start_row - end_row == 1 or (start_row == 6 and start_row - end_row == 2):
                return True
        elif self.color == 'black':
            # 黒のポーンは前方に1マス進むか、初期位置の場合は2マス進むことができる
            if end_row - start_row == 1 or (start_row == 1 and end_row - start_row == 2):
                return True

        else:
            return False
    
    def is_king(self):
        return False