from ..Piece import Piece

class Rook(Piece):
    def __str__(self):
        return 'r' if self.color == 'black' else 'R'

    def is_king(self):
        return False